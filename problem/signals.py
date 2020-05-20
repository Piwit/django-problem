from django.utils import timezone

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Problem


@receiver(pre_save, sender=Problem)
def resolved_at(sender, instance, *args, **kwargs):
    if instance.resolved and instance.resolved_at is None:
        instance.resolved_at = timezone.now()
