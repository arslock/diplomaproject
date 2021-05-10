# Generated by Django 3.1.7 on 2021-04-24 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('submissions', '0003_auto_20210422_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submithomework',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='accounts.studentuser'),
        ),
        migrations.AlterField(
            model_name='submitquiz',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='accounts.studentuser'),
        ),
    ]
