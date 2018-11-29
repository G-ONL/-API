# -*- coding: utf-8 -*-
from django.db import models
from AuthServer.models import Consumer, Seller

# 상품 모델
class Product(models.Model):
    product_name = models.CharField(max_length=45)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_state = models.IntegerField()
    product_url = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


# 결제 정보 모델
class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    payment_type = models.IntegerField()
    payment_state = models.CharField(max_length=20)

    def __str__(self):
        return self.consumer_id.consumer_email + "님의 결제 정보"



# 배송지 모델
class Payment_address(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.consumer_id.consumer_email + "님의 배송지 정보"


# Create your models here.
