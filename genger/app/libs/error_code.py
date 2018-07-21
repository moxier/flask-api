"""
    Created by Amirk on 2018-07-21.
"""
from app.libs.error import APIExcption


class Success(APIExcption):
    code = 201
    error_code = 0
    msg = 'ok'


class ServerError(APIExcption):
    code = 500
    error_code = 1000
    msg = "sorry, we make server unknown error ‘(*>﹏<*)′ "


class ClientTypeError(APIExcption):
    code = 400
    error_code = 1006
    msg = 'client is invalid'


class ParameterException(APIExcption):
    code = 400
    error_code = 10001
