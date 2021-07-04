from django.db import models
from apps.classes.models import Classes
from apps.students.models import Students

class Results(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    marks = models.IntegerField(blank=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Student : {self.student}, Class : {self.class_name}, Position : {self.position}'
