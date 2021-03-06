# Generated by Django 3.1.1 on 2021-02-08 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '__first__'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('marks', models.IntegerField(blank=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
        ),
    ]
