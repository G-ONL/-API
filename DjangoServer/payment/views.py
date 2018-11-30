from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment, Payment_address
from Product.models import Product
from rest_framework import status
from django.forms.models import model_to_dict
from django.db import transaction
from common import const


#시리얼화
def Serializer(request):
    total_price = str(int(request.data['product_price']) * int(request.data['quantity']))
    data = {
        'product_id': request.data['product_id'],
        'consumer_id': request.data['consumer_id'],
        'quantity': request.data['quantity'],
        'total_price': total_price,
        'payment_type': request.data['payment_type'],
        'payment_state': request.data['payment_type']
    }
    return PaymentSerializer(data=data)


#수량체크
def Quantity_check(product_id, quantity):
    product = Product.objects.get(id=product_id)
    if product.product_quantity < int(quantity):
        return False
    else:
        product.product_quantity = product.product_quantity - int(quantity)
        product.save()
        return True


#product_price
@transaction.atomic
@api_view(['POST'])
def Payment_create(request):
    if request.method == 'POST':
        serializer = Serializer(request)
        if serializer.is_valid():
            # 수량체크 로직 돌리기
            check = Quantity_check(request.data['product_id'], request.data['quantity'])
            if check:
                serializer.save()
                payment_id = serializer.data['id']
                payment = Payment.objects.get(id=payment_id)

                product_price = request.data['product_price']
                payment.total_price = int(product_price) * int(payment.quantity)
                payment.save()

                address = request.data['payment_address']
                consumer_id = request.data['consumer_id']
                payment_address = Payment_address(payment_id= payment_id, consumer_id= consumer_id, address=address)
                payment_address.save()
                payment_address_dict = model_to_dict(payment_address)

                return Response({"code":"Success","msg": const.status_code['PAYMENT_CREATE_SUCCESS']['msg'],"results":[serializer.data, payment_address_dict]}, status=status.HTTP_200_OK)
            else:
                return Response({"code": const.status_code['OUTOFSTACK']['code'],
                                 "msg": const.status_code['OUTOFSTACK']['msg']},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"code": const.status_code['PAYMENT_CREATE_FAIL']['code'], "msg": const.status_code['PAYMENT_CREATE_FAIL']['msg']}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Payment_update(request,payment_id):
    if request.method == 'PUT':
        payment_state = request.data['payment_state']
        payment = Payment.objects.get(id=payment_id)
        #payment상태 업데이트
        payment.payment_state = payment_state
        payment.save()
        product_ins = Product.objects.get(id=payment.product_id)

        product = model_to_dict(product_ins)
        payment_obj = model_to_dict(payment)


        return Response({"code": const.status_code['PAYMENT_UPDATE_SUCCESS']['code'],
                         "msg": const.status_code['PAYMENT_UPDATE_SUCCESS']['msg'],"results": [payment_obj,product]}, status=status.HTTP_200_OK)

