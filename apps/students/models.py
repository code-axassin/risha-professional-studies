from datetime import date

from django.db import models

from apps.classes.models import Classes


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    public_id = models.IntegerField(default=500, unique=True)
    name = models.CharField(max_length=200, null=False)
    father_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=125)
    contact = models.IntegerField(null=True)
    father_contact = models.IntegerField(null=True)
    fee = models.IntegerField(null=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    classes = models.ManyToManyField(Classes, blank=True)
    admission_date = models.DateField(null=True)
    admission_end = models.DateField(null=True)
    comments = models.TextField(max_length=250, null=True,blank=True)
    image = models.FileField(null=True, blank=True)
    active = models.BooleanField(null=False, blank=False, default=True)

    @property
    def has_paid(self):
        if date.today() < self.admission_end:
            return True
        else:
            return False


    def save(self, *args, **kwargs):
        "Get last value of Code and Number from database, and increment before save"
        if self.pk ==None and Students.objects.order_by('-public_id').first():
            top = Students.objects.order_by('-public_id').first()
            if self.id == top.id:
                top.admission_date = self.admission_date
                top.admission_end = self.admission_end
                super().save(*args, **kwargs)
            else:
                top = Students.objects.order_by('-public_id').first()
                self.public_id = top.public_id + 1
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Name : {self.name}, F.Name : {self.father_name}"


"""

@receiver(post_save,sender=Students)
def create_public_id(sender,instance,created,**kwargs):
    if created:
            StudentID.objects.create(student=instance)

@receiver(post_save,sender=Students)
def save_user_profile(sender,instance,**kwargs):
        instance.studentid.save()"""