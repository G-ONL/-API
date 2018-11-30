from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment, Payment_address
from Product.models import Product
from rest_framework import status
from django.forms.models import model_to_dict
from django.db import transaction

#수량체크 
def Quantity_check(product_id, quantity):
    product = Product.objects.get(id=product_id)
    if product.product_quantity < int(quantity):
        return False
    else:
        product.product_quantity = product.product_quantity - int(quantity)
        product.save()
        return True

@transaction.atomic
@api_view(['POST'])
def Payment_create(request):
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # 수량체크 로직 돌리기
            check = Quantity_check(request.data['product_id'], request.data['quantity'])
            if check:
                serializer.save()
                address = request.data['payment_address']
                consumer_id = request.data['consumer_id']
                payment_id = serializer.data['id']
                payment_address = Payment_address(payment_id= payment_id, consumer_id= consumer_id, address=address)
                payment_address.save()
                payment_address_dict = model_to_dict(payment_address)
                return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":[serializer.data,payment_address_dict]}, status=status.HTTP_200_OK)
            else:
                return Response({"code": "Fail", "msg": "수량이 부족합니다."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"code": "Fail", "msg": "결제가 실패 되었습니다."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Payment_update(request,payment_id):
    if request.method == 'PUT':
        origin_payment_id = request.data['payment_id']
        # url로 접속한 payment와 요청한 payment가 같은지 확인
        if int(payment_id) == int(origin_payment_id):
            payment_state = request.data['payment_state']
            payment = Payment.objects.get(id=payment_id)
            #payment상태 업데이트
            payment.payment_state = payment_state
            payment.save()
            payment_obj = model_to_dict(payment)
            return Response({"code": "Success", "msg": "결제 정보가 업데이트 되었습니다.","results": payment_obj}, status=status.HTTP_200_OK)
        else:
            return Response({"code": "Fail", "msg": "결제번호가 달라졌습니다."}, status=status.HTTP_400_BAD_REQUEST)


