"""
    Created by Amirk on 2018-07-21.
"""
import json

from flask import request
from werkzeug.exceptions import HTTPException


class APIExcption(HTTPException):
    code = 500
    error_code = 1000
    msg = "sorry, we make server unknown error ‘(*>﹏<*)′ "

    def __init__(self, msg=None, error_code=None, code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIExcption, self).__init__(msg, None)

    def get_body(self, environ=None):
        """Get the json body."""
        result = dict(
            error_code=self.error_code,
            msg=self.msg,
            request=request.method + " " + self.get_url_no_param(),
        )
        return json.dumps(result)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        # print(request.full_path) # /v1/clint/register?
        return full_path.split('?')[0]

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]
