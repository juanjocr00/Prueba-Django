# Generated by Django 4.1.7 on 2023-03-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0009_rename_user_shorterurl_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorterurl',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
