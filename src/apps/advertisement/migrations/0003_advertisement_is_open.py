# Generated by Django 4.1.6 on 2023-05-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='is_open',
            field=models.BooleanField(default=True, verbose_name='Открыто объявление?'),
        ),
    ]