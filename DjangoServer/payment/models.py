# -*- coding: utf-8 -*-
from django.db import models

# 상품 모델
class Product(models.Model):
    product_name = models.CharField(max_length=45)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_state = models.IntegerField()
    product_url = models.CharField(max_length=200)
    seller_id = models.IntegerField()

    def __str__(self):
        return self.product_name


# 결제 정보 모델
class Payment(models.Model):
    product_id= models.IntegerField()
    consumer_id = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    payment_type = models.IntegerField()
    payment_state = models.CharField(max_length=20)


# 배송지 모델
class Payment_address(models.Model):
    consumer_id = models.IntegerField()
    payment_id = models.IntegerField()
    address = models.CharField(max_length=50)

# Create your models here.
