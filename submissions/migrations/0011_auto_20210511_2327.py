# Generated by Django 3.1.7 on 2021-05-11 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0010_auto_20210511_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submitclasswork',
            old_name='homework',
            new_name='classwork',
        ),
    ]