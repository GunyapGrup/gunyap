# Generated by Django 5.0 on 2024-05-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hesap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200, unique=True)),
                ('baglanti', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]