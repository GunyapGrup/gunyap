# Generated by Django 5.0 on 2024-05-12 17:16

import kurumsal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurumsal', '0015_bizkimiz_image_misyonumuz_image_vizyonumuz_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='belge',
            name='kapak_resmi',
            field=models.ImageField(default='kapak/taban.jpeg', upload_to=kurumsal.models.cover_directory_path),
        ),
    ]