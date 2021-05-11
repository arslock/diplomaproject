# Generated by Django 3.1.7 on 2021-05-11 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0010_auto_20210511_2319'),
        ('comments', '0003_auto_20210511_2319'),
        ('classes', '0013_auto_20210511_2319'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeWorkModel',
        ),
        migrations.AddField(
            model_name='classwork',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_work', to='classes.classmodel'),
        ),
    ]
