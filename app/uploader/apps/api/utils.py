from rest_framework import viewsets
from rest_framework.response import Response
from uploader.apps.app import constants


class ModelViewSetPagination(viewsets.ModelViewSet):
    model = None

    def destroy(self, request, *args, **kwargs):
        return Response(constants.FAIL_RESPONSE)

    def update(self, request, *args, **kwargs):
        return Response(constants.FAIL_RESPONSE)

    def get_queryset(self):
        return self.model.objects.filter(**self.get_kwargs_query())

    def get_kwargs_query(self):
        return {}
