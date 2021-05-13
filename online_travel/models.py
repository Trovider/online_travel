from django.db import models


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=10)
    interest_spot = models.CharField(max_length=32, null=True)


class Spot(models.Model):
    spot_name = models.CharField(primary_key=True, max_length=64)
    country_name = models.CharField(max_length=64)
    area_name = models.CharField(max_length=64)


class Video(models.Model):
    spot_name = models.ForeignKey('Spot', db_column='spot_name', on_delete=models.CASCADE)
    url = models.CharField(max_length=128, null=True)


class Livechat(models.Model):
    ip = models.IntegerField(primary_key=True)
    m = models.ForeignKey('Member', on_delete=models.CASCADE)
    access = models.BooleanField()


class Bookmark(models.Model):
    spot_name = models.ForeignKey('Spot', db_column='spot_name', on_delete=models.CASCADE)
    m = models.ForeignKey('Member', on_delete=models.CASCADE)
    memo = models.CharField(max_length=128, null=True)

