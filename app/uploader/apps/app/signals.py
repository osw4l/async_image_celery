import logging
from django.db.models.signals import post_delete
from django.dispatch import receiver
from . import models

logger = logging.getLogger(__name__)

@receiver(post_delete, sender=models.Favorite)
def reassing_priority(sender, instance, *args, **kwargs):
	logger.debug('post delete')
	index = 0
	for fav in models.Favorite.objects.all().order_by('priority'):
		fav.priority = index + 1
		index += 1
		fav.save()
