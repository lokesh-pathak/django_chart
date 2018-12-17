from __future__ import unicode_literals
from django.db import models

# Create your models here.

class SampleData(models.Model):
    age = models.IntegerField(blank=True, null=True)
    workclass = models.CharField(max_length=255, blank=True, null=True)
    fnlwgt = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    education_num = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.CharField(max_length=255, blank=True, null=True)
    race = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    capital_gain = models.IntegerField(blank=True, null=True)
    capital_loss = models.IntegerField(blank=True, null=True)
    hours_per_week = models.IntegerField(blank=True, null=True)
    native_country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'user_data'