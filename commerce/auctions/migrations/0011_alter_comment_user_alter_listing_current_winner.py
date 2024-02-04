# Generated by Django 4.2.9 on 2024-02-04 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_comment_user_alter_listing_current_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='current_winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings_won', to=settings.AUTH_USER_MODEL),
        ),
    ]
