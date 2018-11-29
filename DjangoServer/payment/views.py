from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from .models import Payment
from rest_framework import status


@api_view(['GET'])
def Payment_create(request):
    if request.method == 'GET':
        serializer = PaymentSerializer()
        return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":serializer.data}, status=200)

    #request.data => serial -> is_vaild() 맞으면 넣고 -> 보내줄때는 .data