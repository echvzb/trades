from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    start_bid = models.FloatField()
    created = models.DateField(auto_now=True)
    img_url = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='articles')

    def __str__(self):
        return f"{self.id}: {self.title}"

class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=280)

    def __str__(self):
        return f"{self.auction.id}.{self.id}: {self.text}"
