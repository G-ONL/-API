from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment
from rest_framework import status
from django.forms.models import model_to_dict


@api_view(['POST'])
def Payment_create(request):
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"code": "Fail", "msg": "결제가 실패 되었습니다."},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Payment_update(request,payment_id):
    if request.method == 'PUT':
        origin_payment_id = request.data['payment_id']
        if int(payment_id) == int(origin_payment_id):
            payment_state = request.data['payment_state']
            payment = Payment.objects.get(id=payment_id)
            payment.payment_state = payment_state
            payment.save()
            payment_obj = model_to_dict(payment)
            return Response({"code": "Success", "msg": "결제 정보가 업데이트 되었습니다.","results": request.data}, status=status.HTTP_200_OK)
        else:
            return Response({"code": "Fail", "msg": "결제번호가 달라졌습니다."}, status=status.HTTP_400_BAD_REQUEST)


