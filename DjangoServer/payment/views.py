from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment
from rest_framework import status
from .models import Product
from AuthServer.models import Consumer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET','POST'])
def Payment_create(request):
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"code": "Success", "msg": "결제가 실패 되었습니다."},status=status.HTTP_200_OK)