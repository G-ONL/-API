# -*- coding: utf-8 -*-
from django.db import models


# 결제 정보 모델
class Payment(models.Model):
    product_id= models.IntegerField()
    consumer_id = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    payment_type = models.CharField(max_length=10)
    payment_state = models.CharField(max_length=20)


# 배송지 모델
class Payment_address(models.Model):
    consumer_id = models.IntegerField()
    payment_id = models.IntegerField()
    address = models.CharField(max_length=50)

# Create your models here.
