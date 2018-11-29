# -*- coding: utf-8 -*-

import jwt, datetime

def create_token(query):

    header = {
        "typ": "JWT",
        "alg": "HS256"
    }

    payload = {
        'consumer_id': query.id,
        'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    created_token = jwt.encode(payload, "SECRET_KEY", algorithm='HS256')

    token = {'token': created_token}

    print(created_token.decode('utf-8'))

    return created_token