from django.db import models


class Option(models.Model):

    Time = models.DateTimeField(blank=False)
    Basic1 = models.NullBooleanField(blank=True, null=True, default=None)
    Electrical1 = models.NullBooleanField(blank=True, null=True, default=None)
    Mechanical1 = models.NullBooleanField(blank=True, null=True, default=None)
    Installation1 = models.NullBooleanField(blank=True, null=True, default=None)
    Water1 = models.NullBooleanField(blank=True, null=True, default=None)
    

class Detail(models.Model):

    Basic = models.CharField(max_length=100, blank=True, null=True)
    Electrical = models.CharField(max_length=100, blank=True, null=True)
    Mechanical = models.CharField(max_length=100, blank=True, null=True)
    Installation = models.CharField(max_length=100, blank=True, null=True)
    Water = models.CharField(max_length=100, blank=True, null=True)
    Name = models.CharField(max_length=100)
    