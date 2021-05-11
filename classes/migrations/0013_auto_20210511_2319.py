# Generated by Django 3.1.7 on 2021-05-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_auto_20210511_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('uploaded_file', models.FileField(upload_to='')),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classwork_type', models.CharField(choices=[('lesson', 'lesson'), ('material', 'material'), ('homework', 'homework')], max_length=50)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.RemoveField(
            model_name='homeworkmodel',
            name='scratch_class',
        ),
    ]