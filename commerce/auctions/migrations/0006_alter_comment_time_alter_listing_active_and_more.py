# Generated by Django 4.2.9 on 2024-02-03 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 12, 50, 57, 125145, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(default='oth', max_length=64),
        ),
    ]
