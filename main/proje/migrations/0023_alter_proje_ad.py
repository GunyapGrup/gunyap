# Generated by Django 5.0 on 2024-05-31 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0022_proje_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='ad',
            field=models.CharField(default='Proje Adı', max_length=300),
        ),
    ]
