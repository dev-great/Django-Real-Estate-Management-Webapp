from django.db import models
from datetime import datetime
from django.utils.timezone import timezone


# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default=True)
    city = models.CharField(max_length=100, default=True)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices = (
    ('available', 'Available'),
    ('sold', 'Sold'),
    ('rented', 'Rented')
      ))
    zipcode = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0)
    lot_size = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='media')
    photo_1 = models.ImageField(upload_to='media', blank=True)
    photo_2 = models.ImageField(upload_to='media', blank=True)
    photo_3 = models.ImageField(upload_to='media', blank=True)
    photo_4 = models.ImageField(upload_to='media', blank=True)
    photo_5 = models.ImageField(upload_to='media', blank=True)
    photo_6 = models.ImageField(upload_to='media', blank=True)
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
