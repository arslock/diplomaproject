# Generated by Django 3.1.7 on 2021-05-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_remove_announcment_uploaded_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworkmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]