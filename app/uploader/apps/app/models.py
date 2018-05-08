from django.db import models
from cloudinary.models import CloudinaryField
from . import constants
# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateField(
        auto_now_add=True
    )
    time_created = models.TimeField(
        auto_now_add=True
    )
    last_update = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Ticket(TimeStampModel):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return 'ticket # {} of {}'.format(
            self.id,
            self.user
        )

    def images_count(self):
        return ImageTicket.objects.filter(ticket=self).count()


class ImageTicket(TimeStampModel):
    ticket = models.ForeignKey(
        Ticket,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=30,
        default=constants.INITIAL_STATUS,
        choices=constants.CHOICES_STATUS
    )
    upload = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Image Ticket'
        verbose_name_plural = 'Images Tickets'

    def get_user(self):
        return self.ticket.user.username

    def set_status(self, status):
        self.status = status
        self.save(update_fields=['status'])

    def mark_as_uploaded(self, url):
        self.upload = True
        self.image = url
        self.set_status(constants.UPLOAD_STATUS)
        self.save(update_fields=[
            'upload',
            'image'
        ])

    def get_url(self):
        return self.image.url if self.image else None
