# Generated by Django 3.1 on 2020-09-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200909_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url_name',
            field=models.SlugField(editable=False, max_length=200),
        ),
    ]