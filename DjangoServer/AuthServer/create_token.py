# -*- coding: utf-8 -*-

import jwt, datetime
from AuthServer.logger_handler import LoggerHandler

def create_token(query):

    header = {
        "typ": "JWT",
        "alg": "HS256"
    }

    payload = {
        'consumer_id': query.id,
        'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'iss': 'esp',
        'exp': '1485270000000'
    }

    created_token = jwt.encode(payload, "SECRET_KEY", algorithm='HS256')


    LoggerHandler.server_logger.debug(created_token.decode('utf-8'))


    return created_token