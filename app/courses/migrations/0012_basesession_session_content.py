# Generated by Django 3.1 on 2020-09-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_lecturesession'),
    ]

    operations = [
        migrations.AddField(
            model_name='basesession',
            name='session_content',
            field=models.CharField(default=None, max_length=20000),
            preserve_default=False,
        ),
    ]
