# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from AuthServer.models import Consumer, Seller

# 구매자 Serializer
class ConsumerSerializer(ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'consumer_email', 'consumer_phone')

# 판매자 Serializer
class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'seller_email', 'seller_password')