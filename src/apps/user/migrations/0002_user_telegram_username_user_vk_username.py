# Generated by Django 4.1.6 on 2023-06-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_username',
            field=models.TextField(blank=True, null=True, verbose_name='Имя пользователя в Telegram'),
        ),
        migrations.AddField(
            model_name='user',
            name='vk_username',
            field=models.TextField(blank=True, null=True, verbose_name='Имя пользователя в VK'),
        ),
    ]
