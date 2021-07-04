from django.contrib.auth.models import User
from django.db import models

from apps.students.models import Students


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Students, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)
    date_added = models.DateField()

    def __str__(self):
        return f"Name : {self.student}"
