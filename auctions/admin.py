from django.contrib import admin
from .models import Category, Auction, Comment

class AuctionAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


# Register your models here.
admin.site.register(Category)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Comment)