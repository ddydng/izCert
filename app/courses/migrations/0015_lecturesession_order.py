# Generated by Django 3.1 on 2020-09-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_lecturesession'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturesession',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]