from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'product_id', 'consumer_id', 'payment_date', 'total_price', 'payment_type', 'payment_state')