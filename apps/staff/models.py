from django.db import models
from django.utils import timezone


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    contact = models.CharField(max_length=200, null=False)
    cv = models.FileField(null=True, blank=True)
    comments = models.TextField(max_length=255, null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.name}"