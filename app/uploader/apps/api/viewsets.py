import os
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from uploader.apps.app.models import ImageTicket, Ticket
from uploader.apps.app.tasks import upload_image
from django.conf import settings
from . import serializers, utils


class ImageTicketViewSet(utils.ModelViewSetPagination):
    serializer_class = serializers.ImageTicketSerializer
    queryset = ImageTicket.objects.all()
    model = ImageTicket
    parser_classes = (MultiPartParser, FormParser,)

    def get_kwargs_query(self):
        return {'ticket__user': self.request.user}

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        response = {}
        current_status = status.HTTP_202_ACCEPTED
        if images:
            ticket = Ticket.objects.create(user_id=request.user.id)
            for image in images:
                path = default_storage.save('tmp/' + str(image), ContentFile(image.read()))
                tmp_file_path = os.path.join(settings.MEDIA_ROOT, path)
                upload_image.delay(tmp_file_path, ticket.id)
            current_status = status.HTTP_201_CREATED
            response['success'] = True
        else:
            response['success'] = False
        return Response(response, status=current_status)


class TicketViewSet(utils.ModelViewSetPagination, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.TicketSerializer
    queryset = Ticket.objects.all()
    model = Ticket

    def create(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_kwargs_query(self):
        return {'user': self.request.user}
