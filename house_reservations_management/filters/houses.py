from datetime import datetime as Datetime, timedelta

from django.db.models import QuerySet
from django.utils.timezone import now
from rest_framework import exceptions
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request

from house_reservations_management.services.reservations_overlapping import filter_for_available_houses_by_period


class HousesAvailableByDateFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet, view):
        query_params = request.query_params
        try:
            check_in_date = Datetime.strptime(query_params.get("check_in_date"), "%d-%m-%Y").date()
            check_out_date_str = query_params.get("check_out_date")
            if check_out_date_str is None:
                check_out_date = check_in_date + timedelta(days=1)
            else:
                check_out_date = Datetime.strptime(check_out_date_str, "%d-%m-%Y").date()

            if not now().date() < check_in_date < check_out_date:
                # если прилетели неправильные даты check_in и check_out или
                # если пытаются забронировать что-то на прошедшую дату
                raise exceptions.ValidationError("Некорректные даты бронирования. "
                                              "Не выполнено неравенство now < check_in_date < check_out_date: "
                                              f"{now().date().strftime('%d-%m-%Y')} < "
                                              f"{check_in_date.strftime('%d-%m-%Y')} < "
                                              f"{check_out_date.strftime('%d-%m-%Y')}")

            queryset = filter_for_available_houses_by_period(queryset, check_in_date, check_out_date)

        except TypeError:
            # если нет какой-то из дат - мы не можем фильтровать
            # также если проблема с порядком дат "now < in < out" попадаем сюда же
            pass

        return queryset
