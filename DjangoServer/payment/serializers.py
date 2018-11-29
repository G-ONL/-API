from .models import Payment,Product
from AuthServer.models import Consumer, Seller
from rest_framework import serializers


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ('seller_email','seller_password')


class ConsumerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumer
        fields = ('consumer_email','consumer_phone')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name','product_price','product_quantity', 'product_state', 'product_url', 'seller_id')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('product_id', 'consumer_id', 'payment_date', 'total_price', 'payment_type', 'payment_state')