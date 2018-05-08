from rest_framework import generics
from . import serializers
from uploader.apps.app.models import Ticket, ImageTicket


class TicketListApiView(generics.ListAPIView):
    serializer_class = serializers.ImageTicketSerializer
    queryset = ImageTicket.objects.all()
    model = ImageTicket

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status = self.request.query_params.get('status', None)
        query_kwargs = {}

        if status:
            query_kwargs['status__icontains'] = status
        if start_date and end_date:
            query_kwargs['created__range'] = [start_date, end_date]
        elif start_date and not end_date:
            query_kwargs['created__gte'] = start_date
        elif end_date and not start_date:
            query_kwargs['created__lte'] = end_date
        return qs.filter(ticket__user=self.request.user, **query_kwargs)



