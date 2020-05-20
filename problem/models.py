from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .settings import PAGES


class AbstractProblem(models.Model):
    page = models.CharField(max_length=255,choices=PAGES)
    problem = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} by {} - {}'.format(self.page, self.user.username, self.reported_at)


class Problem(AbstractProblem):
    pass
