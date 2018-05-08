from rest_framework import serializers
from uploader.apps.app import models


class ImageTicketSerializer(serializers.ModelSerializer):

    url = serializers.ReadOnlyField(source='get_url')
    username = serializers.ReadOnlyField(source='ticket.user.username')
    user = serializers.ReadOnlyField(source='ticket.user.id')

    class Meta:
        model = models.ImageTicket
        fields = ('id', 'ticket', 'status', 'user', 'url', 'created', 'username')


class TicketSerializer(serializers.ModelSerializer):
    images = ImageTicketSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('id', 'created', 'user', 'images')
