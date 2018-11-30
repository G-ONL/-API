const_value = {
    'TTL': 300,
    'HEADER_DOES_NOT_EXIST': 'NO_token_in_header',
    'SESSION_EXIST': 'Session_exist',
    'SESSION_CREATED': 'Session_created',
    'SESSION_DOES_NOT_EXIST': 'Session does not exist',
    'SESSION_EXPIRE': 'Session expired',
    'TOKEN_DOES_NOT_EXIST': 'Token does not exist'
}


status_code = {
    'SUCCESS' :{
            "code" : 1,
            "msg": "Request Sucess",
            "data": ""
    },

    'FAIL': {
        "code": 0,
        "msg": "Request Failure",
        "data": ""
    },

    'CONSUMER_SIGNUP_SUCCESS' : {
        "code": 1200,
        "msg": "구매자 회원 가입에 성공했습니다.",
        "results": []
    },

    'CONSUMER_WRONG_PARAMETER': {
        "code": 1401,
        "msg": "구매자 회원 가입에서 옳지 않은 파라미터를 보내셨습니다.",
        "results": []
    },

    'CONSUMER_SIGNUP_INVALID_EMAIL' : {
        "code": 1402,
        "msg": "잘못된 이메일입니다.",
        "results" : []
    },

    'CONSUMER_GET_LIST': {
        "code": 1201,
        "msg": "구매자 조회에 성공했습니다.",
        "results": []
    },

    'CONSUMER_GET_LIST_FAILURE': {
        "code": 1403,
        "msg": "구매자 조회에 실패했습니다.",
        "results": []
    },

    'CONSUMER_SIGNIN_SUCCESS': {
        "code": 1202,
        "msg": "구매자 로그인에 성공했습니다.",
        "results": []
    },

    'CONSUMER_SIGNIN_INVALID_EMAIL': {
        "code": 1202,
        "msg": "구매자 로그인에 실패했습니다.",
        "results": []
    },
    'CONSUMER_SIGNIN_INVALID_PHONE': {
        "code": 1405,
        "msg": "구매자 로그인에 실패했습니다. 유효하지 않은 전화번호입니다.",
        "results": []
    },

}