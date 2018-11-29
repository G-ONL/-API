# -*- coding: utf-8 -*-

import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from AuthServer.models import Seller, Consumer
from AuthServer.serializers import SellerSerializer, ConsumerSerializer
from AuthServer.create_token import create_token
from common.const import status_code,const_value



# 판매자 회원 가입 - csrf 때문에 Function Based View로 구현
@api_view(['GET','POST']) # GET 과 POST로 요청 가능
@csrf_exempt
def seller_signup(request):
    if request.method == 'POST': # [POST] 판매자 회원 가입
        received_data = json.dumps(request.data) # 들어온 request data 확인
        print(received_data) # 받은 data 확인

        serializer = SellerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # TODO 회원 가입 인증 메일 발송 (먼저 DB에 넣고 인증 메일 발송할건지, or 인증메일 발송 없이 회원 가입 할건지? - 안하기로 함!!

            results = serializer.data

            return Response(
                {
                    "code" : status_code['CONSUMER_SIGNUP_SUCCESS'],
                    "message" : status_code['CONSUMER_SIGNUP_SUCCESS'],
                    "results" : results
                },
                status=status.HTTP_200_OK)

        return Response({"code" : "Failure" , "message" : "Seller Signup Failed"}, status=status.HTTP_200_OK )

    else: # [GET] 가입된 모든 판매자 일단 출력
        serializer = SellerSerializer(Seller.objects.all(), many=True)
        result_msg = serializer.data
        return Response({"code" : "Success", "message" : "Get Seller data", "result" : result_msg}, status=status.HTTP_200_OK)



# 판매자 로그인  - csrf 때문에 Function Based View로 구현
@api_view(['POST'])
@csrf_exempt
def seller_signin(request):
    if request.method == 'POST':
        try:
            received = json.dumps(request.data)
            print(received)

            seller_query = Seller.objects.get(seller_email=request.data['seller_email'])

        except Seller.DoseNotExist:
            return Response({"code" : "Failure", "message" : "Invalid Seller Email"} , status=status.HTTP_200_OK)

        # 패스워드 까지 일치하여 판매자 로그인 성공
        if request.data['seller_password'] == seller_query.seller_password:
            token = create_token(seller_query)

            token_result_msg = {'Token': token, 'seller_id': seller_query.id,
                                                    'seller_email': seller_query.seller_email}
            # Client 에게 토큰을 json에 담아 보냄

            print(token_result_msg)

            send_data = {'Token': token, 'User': seller_query}

        else:
            return Response({"code" : "Failure", "message" : "Invalid Seller Password"} , status=status.HTTP_200_OK)


# 구매자 회원 가입  - csrf 때문에 Function Based View로 구현
@api_view(['GET','POST'])
@csrf_exempt
def consumer_signup(request):
    if request.method == 'POST': # [POST] 구매자 회원 가입
        received = json.dumps(request.data) # 들어온 request data 확인
        print(received) # 받은 data

        serializer = ConsumerSerializer(data=request.data)

        if serializer.is_valid(): # data가 Model에 추가될 수 있는지 확인
            print("is_valid()지롱")
            serializer.save()

            # TODO 회원 가입 인증 메일 발송 (먼저 DB에 넣고 인증 메일 발송할건지, or 인증메일 발송 없이 회원 가입 할건지?- 안하기로 함!

            result_msg = serializer.data

            return Response(
                {
                    "code" : status_code['CONSUMER_SIGNUP_SUCCESS']['code'],
                    "message": status_code['CONSUMER_SIGNUP_SUCCESS']['msg'],
                    "result" : result_msg
                },
                status=status.HTTP_200_OK)

        return Response(
            {
                "code" : status_code['CONSUMER_WRONG_PARAMETER']['code'],
                "message" : status_code['CONSUMER_WRONG_PARAMETER']['msg'],
                "result" : request.data
            },
            status=status.HTTP_200_OK)

    else: # [GET] 가입된 모든 구매자 일단 출력
        serializer = ConsumerSerializer(Consumer.objects.all(), many=True)
        result_msg = serializer.data
        return Response({"code" : "Success", "message" : "Get Consumer data", "result" : result_msg}, status=status.HTTP_200_OK)

# 구매자 로그인  - csrf 때문에 Function Based View로 구현
@api_view(['POST'])
@csrf_exempt
def consumer_signin(request):
    if request.method == 'POST':
        try:
            received = json.dumps(request.data)
            print(received)

            consumer_query = Consumer.objects.get(seller_email=request.data['consumer_email'])

        except Consumer.DoseNotExist:
            return Response({"code" : "Failure", "message" : "Invalid Consumer Email"} , status=status.HTTP_200_OK)

        # phone 까지 일치하여 판매자 로그인 성공
        if request.data['consumer_phone'] == consumer_query.consumer_phone:
            token = create_token(consumer_query)

            token_result_msg = {'Token': token, 'seller_id': consumer_query.id,
                                                    'seller_email': consumer_query.seller_email}

            # Client 에게 토큰을 json에 담아 보냄

            print(token_result_msg)

            send_data = {'Token': token, 'User': consumer_query}

        else:
            return Response({"code" : "Failure", "message" : "Invalid Consumer Password"} , status=status.HTTP_200_OK)
