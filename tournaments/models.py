from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True) # optional field
    type = models.TextField(default='League')