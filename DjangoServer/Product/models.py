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

# Create your models here.
