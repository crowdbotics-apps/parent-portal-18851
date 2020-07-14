from django.conf import settings
from django.db import models


class Location(models.Model):
    "Generated Model"
    amenities = models.TextField(null=True, blank=True,)


class VendorDetail(models.Model):
    "Generated Model"
    website = models.URLField()
    description = models.TextField()
    associated_name = models.TextField(null=True, blank=True,)


class Sponsor(models.Model):
    "Generated Model"
    name = models.TextField()
    logo_image = models.SlugField(max_length=50,)
    sponsor_level = models.TextField()
    presenter = models.BooleanField()
    website = models.URLField(null=True, blank=True,)


class Presenter(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    title = models.CharField(max_length=256,)


class Vendor(models.Model):
    "Generated Model"
    logo_image = models.SlugField(null=True, blank=True, max_length=50,)


class Schedule(models.Model):
    "Generated Model"
    dateTime = models.DateTimeField()
    description = models.TextField(null=True, blank=True,)
    track = models.TextField(null=True, blank=True,)


class MySchedule(models.Model):
    "Generated Model"
    pp = models.BigIntegerField(null=True, blank=True,)


class Category(models.Model):
    "Generated Model"
    description = models.TextField()
    name = models.CharField(null=True, blank=True, max_length=256,)


class Favorites(models.Model):
    "Generated Model"
    jk = models.BigIntegerField(null=True, blank=True,)


class Faq(models.Model):
    "Generated Model"
    description = models.TextField()


# Create your models here.
