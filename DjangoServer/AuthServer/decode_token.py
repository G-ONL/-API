# -*- coding: utf-8 -*-

import jwt, datetime
from AuthServer.logger_handler import server_logger

def decode_token(token):


    get_user_id_from_token = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])

    print(get_user_id_from_token)

    return None