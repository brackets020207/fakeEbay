from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    category = models.CharField(max_length = 64)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    image_url = models.CharField(max_length = 500, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="listings")


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name= 'bids')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete = models.CASCADE,  related_name='bids')

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name= 'comments')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')