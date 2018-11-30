from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'product_id', 'consumer_id','quantity','total_price' ,'payment_date', 'payment_type', 'payment_state')