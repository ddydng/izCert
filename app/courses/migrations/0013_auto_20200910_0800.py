# Generated by Django 3.1 on 2020-09-10 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_basesession_session_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturesession',
            name='basesession_ptr',
        ),
        migrations.DeleteModel(
            name='BaseSession',
        ),
        migrations.DeleteModel(
            name='LectureSession',
        ),
    ]