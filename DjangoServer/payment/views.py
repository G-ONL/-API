from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def Payment_create(request):
    if request.method == 'GET':
        return Response({"code":"Success","msg":"결제 정보가 생성이 되었습니다.","results":[PaymentSerializer]}, status=200)