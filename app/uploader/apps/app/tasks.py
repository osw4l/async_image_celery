import logging, os
from celery import shared_task, task
from uploader.apps.app.models import ImageTicket
from uploader.celery_conf import app
from cloudinary import uploader
from . import constants

logger = logging.getLogger(__name__)


@shared_task
def add(x, y):
    return x + y


@app.task
def upload_image(path, ticket):
    image_ticket = ImageTicket.objects.create(ticket_id=ticket)
    try:
        image_ticket.set_status(constants.UPLOADING_STATUS)
        image = uploader.upload(path)
        if image:
            image_ticket.mark_as_upload()
            image_ticket.image = image['url']
            image_ticket.save()
    except:
        image_ticket.set_status(constants.FAIL_STATUS)
    os.remove(path)
