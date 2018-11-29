# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# 구매자 모델
class Consumer(models.Model):
    consumer_email = models.CharField(max_length=45, unique=True)
    consumer_phone = models.CharField(max_length=11)

    def __str__(self):
        return self.consumer_email

# 판매자 모델
class Seller(models.Model):
    seller_email = models.CharField(max_length=45, unique=True)
    seller_password = models.CharField(max_length=45)

    def __str__(self):
        return self.seller_email