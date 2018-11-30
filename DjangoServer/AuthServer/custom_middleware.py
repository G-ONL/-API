# -*- coding: utf-8 -*-

from rest_framework import exceptions, status
from rest_framework.response import Response
from common.const import const_value, status_code
from AuthServer.split_header import split_header
from django.http import JsonResponse
from AuthServer.logger_handler import LoggerHandler
from AuthServer.decode_token import decode_token


class TokenMiddleware(object):
    def __init__(self, get_response=None):
        LoggerHandler.server_logger.debug('Middleware init')

        self.get_response = get_response

    def __call__(self, request):
        # print("[[TokenMiddleware]] __call__")
        LoggerHandler.server_logger.debug('[[TokenMiddleware]] __call__')
        allowed_ips = ['127.0.0.1', '0.0.0.0']

        ip = request.META.get('REMOTE_ADDR')

        # 고객 정보 API에 대해 모두 토큰 인증 절차 안거침
        if request.path.startswith('/users/consumer/'):
            response = self.get_response(request)
            return response

        # 결제 API에 대해 모두 토큰 인증 절차 거침
        else:
            token = split_header(request)

            # 헤더에 토큰이 없으므로 인증된 사용자의 접근이 아님
            if token is None:
                LoggerHandler.server_logger.debug("token is None")

                status_code['FAIL']['data'] = const_value['HEADER_DOES_NOT_EXIST']
                return JsonResponse(
                    {
                        "code": status_code['FAIL']['code'],
                        "msg" : status_code['FAIL']['data']
                    },
                    status=status.HTTP_200_OK
                )

            # 헤더에 토큰 있으면 일단 인증된 사용자의 접근이라고 식별
            else:
                LoggerHandler.server_logger.debug("Token exist")

                if decode_token(token): # 토큰 내에 consumer_id 있음

                    status_code['SUCCESS']['data'] = const_value['SESSION_EXIST']

                    # TODO Redis에 해당 토큰 있는지 검사

                    return JsonResponse(
                            {
                                "code" : status_code['SUCCESS']['code'],
                                "msg" : status_code['SUCCESS']['data']
                            },
                            status=status.HTTP_200_OK
                        )
                else: # 토큰이 있지만 유효한 토큰이 아님
                    status_code['FAIL']['data'] = const_value['SESSION_DOES_NOT_EXIST']

                    return JsonResponse(
                        {
                            "code": status_code['FAIL']['code'],
                            "msg": status_code['FAIL']['data']
                        },
                            status=status.HTTP_401_UNAUTHORIZED
                        )