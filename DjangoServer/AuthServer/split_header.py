# -*- coding: utf-8 -*-

import jwt, datetime
from common.const import const_value, status_code
from AuthServer.logger_handler import LoggerHandler

# 토큰 관련 클래스 - 헤더에 담긴 토큰 가져오기


# 헤더에 담긴 토큰 가져오기 (사용자가 보낸 토큰)
def split_header(request):
    LoggerHandler.server_logger.debug('Split Request Header')

    # 헤더에 토큰이 있으면 가져오고, 없으면 None
    header_token = request.META.get('HTTP_AUTHORIZATION', None)

    if header_token is None: #헤더에 토큰이 없음
        LoggerHandler.server_logger.debug('Token does not exist in header')
        return None

    else: #헤더에 토큰이 있어서 parsing 필요
        splited_token = header_token.split(' ')[1]

        LoggerHandler.server_logger.debug("split header token" + splited_token)

        return splited_token