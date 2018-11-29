# -*- coding: utf-8 -*-

from rest_framework import exceptions, status
from rest_framework.response import Response
from common.const import const_value, status_code
from AuthServer.split_header import split_header
from django.http import JsonResponse
from AuthServer.logger_handler import server_logger
from AuthServer.decode_token import decode_token


class TokenMiddleware(object):
    def __init__(self, get_response=None):
        server_logger.debug('Middleware init')

        self.get_response = get_response

    def __call__(self, request):
        # print("[[TokenMiddleware]] __call__")
        server_logger.debug('[[TokenMiddleware]] __call__')
        allowed_ips = ['127.0.0.1', '0.0.0.0']

        ip = request.META.get('REMOTE_ADDR')

        # 결제 API에 대해 모두 토큰 인증 절차 거침
        if request.path.startswith('/payments/'):
            response = self.get_response(request)
            return response

        else:
            token = split_header(request)

            # 헤더에 토큰이 없으므로 인증된 사용자의 접근이 아님
            if token is None:
                server_logger.debug("token is None")

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
                try:
                    server_logger.debug("Token exist")

                    decode_token(token)

                    status_code['SUCCESS']['data'] = const_value['SESSION_EXIST']

                    # TODO Redis에 해당 토큰 있는지 검사

                    return JsonResponse(
                        {
                            "code" : status_code['SUCCESS']['code'],
                            "msg" : status_code['SUCCESS']['data']
                        },
                        status=status.HTTP_200_OK
                    )
                except:
                    status_code['FAIL']['data'] = const_value['SESSION_DOES_NOT_EXIST']

                    return JsonResponse(
                        {
                            "code" : status_code['FAIL']['code'],
                            "msg" : status_code['FAIL']['data']
                        },
                        status=status.HTTP_401_UNAUTHORIZED
                    )