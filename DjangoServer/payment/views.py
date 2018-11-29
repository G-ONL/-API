from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment
from rest_framework import status
from .models import Product
from AuthServer.models import Consumer


@api_view(['GET','POST'])
def Payment_create(request):
    if request.method == 'GET':
        serializer = PaymentSerializer()
        return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':


        serializer = PaymentSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":serializer.data}, status=status.HTTP_200_OK)

    #request.data => serial -> is_vaild() 맞으면 넣고 -> 보내줄때는 .data