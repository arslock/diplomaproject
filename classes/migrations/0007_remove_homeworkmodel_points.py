# Generated by Django 3.1.7 on 2021-04-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_aboutclass_syllabus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkmodel',
            name='points',
        ),
    ]
