from __future__ import unicode_literals
from django.db import models


class History(models.Model):
    history_url = models.CharField(max_length=200)
    history_title = models.TextField(null=True)

    def __str__(self):
        return self.history_title
