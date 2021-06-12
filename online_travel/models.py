from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=10)
    interest_spot = models.CharField(max_length=32, null=True)


class Spot(models.Model):
    spot_name = models.CharField(primary_key=True, max_length=64)
    country_name = models.CharField(max_length=64)
    area_name = models.CharField(max_length=64)
    link = models.URLField(null=True)
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='description')
    def __str__(self):
        return self.spot_name


class Video(models.Model):
    spot_name = models.ForeignKey('Spot', db_column='spot_name', on_delete=models.CASCADE)
    url = models.CharField(max_length=128, null=True,  blank=True)


class Livechat(models.Model):
    ip = models.IntegerField(primary_key=True)
    m = models.ForeignKey('Member', on_delete=models.CASCADE)
    access = models.BooleanField()


class Bookmark(models.Model):
    spot_name = models.ForeignKey('Spot', db_column='spot_name', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo = models.CharField(max_length=128, null=True)


class Photo(models.Model):
    spot_name = models.ForeignKey('Spot', db_column='spot_name', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
