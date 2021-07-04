from django.db import models
from apps.staff.models import Staff


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    #course = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=150, null=True)
    rom_no = models.CharField(max_length=150, null=True, blank=True)
    timing = models.TimeField(null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return f'Class : {self.name}, Timing : {self.timing}, Instructor : {self.staff}'
