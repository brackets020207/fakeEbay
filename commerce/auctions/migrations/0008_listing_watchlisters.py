# Generated by Django 4.2.9 on 2024-02-04 00:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlisters',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
