# Generated by Django 3.1.7 on 2021-04-20 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20210420_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutclass',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_class', to='classes.classmodel'),
        ),
        migrations.AlterField(
            model_name='announcment',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcment_class', to='classes.classmodel'),
        ),
        migrations.AlterField(
            model_name='homeworkmodel',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_class', to='classes.classmodel'),
        ),
        migrations.AlterField(
            model_name='lessonmodel',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_class', to='classes.classmodel'),
        ),
        migrations.AlterField(
            model_name='materialmodel',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_class', to='classes.classmodel'),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='scratch_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_class', to='classes.classmodel'),
        ),
    ]
