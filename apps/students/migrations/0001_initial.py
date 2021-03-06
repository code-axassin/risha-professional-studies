# Generated by Django 3.1.1 on 2021-02-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('public_id', models.IntegerField(default=500, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=125)),
                ('contact', models.IntegerField(null=True)),
                ('father_contact', models.IntegerField(null=True)),
                ('fee', models.IntegerField(null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('admission_date', models.DateField(null=True)),
                ('admission_end', models.DateField(null=True)),
                ('comments', models.TextField(blank=True, max_length=250, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('classes', models.ManyToManyField(blank=True, to='classes.Classes')),
            ],
        ),
    ]
