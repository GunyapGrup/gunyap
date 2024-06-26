# Generated by Django 5.0 on 2024-05-22 10:46

import proje.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0016_alter_proje_kapak_resmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='ad',
            field=models.CharField(default='Proje Adı', max_length=200),
        ),
        migrations.AlterField(
            model_name='proje',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='proje',
            name='ozet',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projeresim',
            name='image',
            field=models.ImageField(null=True, upload_to=proje.models.proje_ust_path),
        ),
    ]
