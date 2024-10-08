import logging

from django.conf import settings

from house_reservations.models import HouseReservation
from notifications.common.url import media_url_by_path
from .new_reservation_templates import *

HOUSE_LOCATION_LINK = "https://yandex.ru/maps/?ll=35.599293%2C54.748715&mode=whatshere&whatshere%5Bpoint%5D=35.599179" \
                      "%2C54.748626&whatshere%5Bzoom%5D=17.871925&z=17"
HOUSE_LOCATION_TEXT = "Деревня Никола-Ленивец, 10, сельское поселение Угорское, Дзержинский район, Калужская область"

logger = logging.getLogger(__name__)


class NewReservationTemplateBuilder:
    def build(self, reservation: HouseReservation) -> str:
        house_data_html = self._build_house_data(reservation)
        reservation_data_html = self._build_reservation_data(reservation)
        reservation_comment_html = self._build_comment_html(reservation)
        bill_html = self._build_bill_html(reservation)

        return MAIN_TEMPLATE.format(
            main_template_styles=MAIN_TEMPLATE_STYLE,
            house_data=house_data_html,
            reservation_data=reservation_data_html,
            comment=reservation_comment_html,
            bill=bill_html,
        )

    def _build_house_data(self, reservation: HouseReservation) -> str:
        house_image_path = reservation.house.pictures.first().picture.path

        house_data_html = HOUSE_DATA_TEMPLATE.format(
            style=SINGLE_BLOCK_STYLE,
            house_location_icon="https://cdn-icons-png.flaticon.com/512/5192/5192571.png",
            house_image=media_url_by_path(house_image_path),
            house_location_link=HOUSE_LOCATION_LINK,
            house_location_text=HOUSE_LOCATION_TEXT,
        )

        return house_data_html

    def _build_reservation_data(self, reservation: HouseReservation) -> str:
        check_in_datetime_icon_path = RESERVATION_TIME_IMAGE_PATH[reservation.local_check_in_datetime.time()]
        check_out_datetime_icon_path = RESERVATION_TIME_IMAGE_PATH[reservation.local_check_out_datetime.time()]

        reservation_data_html = HOUSE_RESERVATION_DATA_TEMPLATE.format(
            style=SINGLE_BLOCK_STYLE,
            house_name=reservation.house.name,
            check_in_day=reservation.check_in_datetime.strftime('%d-%m-%Y'),
            check_in_datetime_icon=media_url_by_path(check_in_datetime_icon_path),
            check_in_time=reservation.check_in_datetime.strftime('%H:%M'),
            check_out_day=reservation.check_out_datetime.strftime('%d-%m-%Y'),
            check_out_datetime_icon=media_url_by_path(check_out_datetime_icon_path),
            check_out_time=reservation.check_out_datetime.strftime('%H:%M'),
            first_name=reservation.client.first_name,
            last_name=reservation.client.last_name,
            email=reservation.client.email,
            contact=reservation.preferred_contact,
            reservation_url=f"https://{settings.ALLOWED_HOSTS[0]}/reservation/{reservation.slug}",
            reservation_slug=reservation.slug,
            total_price=reservation.bill.total,
        )

        return reservation_data_html

    def _build_comment_html(self, reservation: HouseReservation) -> str:
        reservation_comment_html = ""
        if reservation.comment:
            reservation_comment_html = COMMENT_TEMPLATE.format(
                style=SINGLE_BLOCK_STYLE,
                reservation_comment=reservation.comment,
            )

        return reservation_comment_html

    def _build_bill_html(self, reservation: HouseReservation) -> str:
        all_bill_positions = reservation.bill.chronological_positions + reservation.bill.non_chronological_positions

        bill_positions_html = []

        for position in all_bill_positions:
            bill_positions_html.append(
                BILL_POSITION_TEMPLATE.format(
                    bill_position_icon=media_url_by_path(BILL_POSITION_IMAGE_PATH[position["type"]]),
                    bill_position_description=position["description"],
                    bill_position_price=position["price"],
                )
            )

        bill_html = BILL_TEMPLATE.format(
            style=SINGLE_BLOCK_STYLE,
            bill_positions="".join(bill_positions_html),
        )

        return bill_html
