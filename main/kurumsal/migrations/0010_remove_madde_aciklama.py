# Generated by Django 5.0 on 2024-05-05 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurumsal', '0009_alter_madde_aciklama'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madde',
            name='aciklama',
        ),
    ]
