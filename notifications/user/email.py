import logging
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from house_reservations.models import HouseReservation
from notifications.user.email_templates.new_reservation.template_builder import NewReservationTemplateBuilder
from notifications.user.general import UserNotificationsBaseClass

logger = logging.getLogger(__name__)


class UserNotificationsEmail(UserNotificationsBaseClass):
    email_login: str
    email_password: str
    new_reservation_template_builder: NewReservationTemplateBuilder

    def __init__(
            self,
            email_login: str,
            email_password: str,
            new_reservation_template_builder: NewReservationTemplateBuilder,
    ):
        self.email_login = email_login
        self.email_password = email_password
        self.new_reservation_template_builder = new_reservation_template_builder

    def send_email(self, message):
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()
        smtp_object.login(self.email_login, self.email_password)

        return smtp_object.send_message(msg=message)

    def new_reservation_created(self, reservation: HouseReservation):
        new_reservation_html = self.new_reservation_template_builder.build(reservation)

        msg = MIMEMultipart('related')
        msg['Subject'] = f'Вы забронировали домик "{reservation.house.name}"'
        msg['From'] = self.email_login
        msg['To'] = reservation.client.email

        msg.attach(MIMEText(new_reservation_html, 'html'))

        self.send_email(msg)
