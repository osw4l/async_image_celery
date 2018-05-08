from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = 'Uploader '
admin.site.site_title = 'Uploader '
admin.site.index_title = 'Uploader'


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'user',
                    'time_created', 'last_update']


@admin.register(models.ImageTicket)
class ImageTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'get_user',
                    'get_url', 'status', 'already_upload',
                    'time_created', 'last_update']

