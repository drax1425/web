# Generated by Django 5.0.6 on 2024-06-28 08:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodista',
            name='imagen',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='imagen'),
            preserve_default=False,
        ),
    ]
