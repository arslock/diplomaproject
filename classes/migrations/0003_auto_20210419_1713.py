# Generated by Django 3.1.7 on 2021-04-19 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('classes', '0002_auto_20210419_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='accounts.teacheruser'),
            preserve_default=False,
        ),
    ]
