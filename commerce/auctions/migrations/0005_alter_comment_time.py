# Generated by Django 4.2.9 on 2024-02-03 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 10, 3, 39, 169863, tzinfo=datetime.timezone.utc)),
        ),
    ]
