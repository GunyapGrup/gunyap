# Generated by Django 5.0 on 2024-05-12 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurumsal', '0020_sayaç_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sayaç',
            old_name='çalışan',
            new_name='calisan',
        ),
        migrations.RenameField(
            model_name='sayaç',
            old_name='müşteri',
            new_name='musteri',
        ),
    ]
