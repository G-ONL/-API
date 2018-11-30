# -*- coding: utf-8 -*-

import jwt, datetime
from AuthServer.logger_handler import LoggerHandler

def decode_token(token):


    get_user_id_from_token = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])

    # print(get_user_id_from_token)

    # print(get_user_id_from_token['consumer_id'])

    LoggerHandler.server_logger.debug(get_user_id_from_token)
    LoggerHandler.server_logger.debug(get_user_id_from_token['consumer_id'])

    return get_user_id_from_token['consumer_id']