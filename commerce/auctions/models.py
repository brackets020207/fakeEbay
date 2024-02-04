from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    category = models.CharField(max_length = 64, default = "oth")
    description = models.TextField()
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    image_url = models.CharField(max_length = 500, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="listings")
    active = models.BooleanField(default=True)
    current_winner = models.ForeignKey(User, on_delete = models.CASCADE, related_name="listings_won", null = True)
    watchlisters = models.ManyToManyField(User, blank=True, related_name="watchlist")


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name= 'bids')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete = models.CASCADE,  related_name='bids')

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name= 'comments')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments', null = True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)