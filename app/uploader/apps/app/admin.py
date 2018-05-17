from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = 'Uploader '
admin.site.site_title = 'Uploader '
admin.site.index_title = 'Uploader'


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'user',
                    'time_created', 'last_update', 'images_count']


@admin.register(models.ImageTicket)
class ImageTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'ticket', 'get_user',
                    'get_url', 'status', 'upload',
                    'time_created', 'last_update']


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'priority']

