from django.db import models
from django.urls import reverse_lazy
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

    def data(self):
        return self.__str__()

    def get_images(self):
        return  ImageTicket.objects.filter(
            ticket=self
        )

    def images_count(self):
        return self.get_images().count()

    def get_absolute_url(self):
        return reverse_lazy(
            'app:ticket', 
            kwargs={
            'pk': self.pk
        })


class Favorite(TimeStampModel):
    user = models.OneToOneField(
        'auth.User',
        unique=True,
        on_delete=models.CASCADE
    )
    priority = models.PositiveIntegerField(
        default=0,
        unique=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def save(self, *args, **kwargs):
        if not self.id:
            self.priority = self.count_records() + 1
        super().save(*args, **kwargs)

    @staticmethod
    def count_records():
        return Favorite.objects.all().count()


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
