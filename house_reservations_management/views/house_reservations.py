from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.mixins import ByActionMixin
from house_reservations.models import HouseReservation
from house_reservations_billing.serializers import HouseReservationWithBillSerializer
from houses.models import House


class HouseReservationsViewSet(ByActionMixin,
                               mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    serializer_classes_by_action = {
        "default": None,
    }
    queryset = House.objects.filter(active=True)

    # TODO list reservations by period
    # TODO list reservations by house ???
    # TODO get reservation by slug (lookup field)

    @action(methods=['get'], url_path='by_slug', detail=False)
    def retrieve_reservation_by_slug(self, request):
        reservation = HouseReservation.objects.get(slug=request.GET.get('slug'))

        if reservation:
            return Response({"reservation": HouseReservationWithBillSerializer(reservation).data}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
