# Generated by Django 5.0 on 2024-05-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0002_rename_açıklama_proje_aciklama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='baslik',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
