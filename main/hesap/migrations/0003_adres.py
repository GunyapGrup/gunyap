# Generated by Django 5.0 on 2024-05-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesap', '0002_mail_telefon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=300, unique=True)),
            ],
        ),
    ]
