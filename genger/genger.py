"""
    Created by Amirk on 2018-07-20.
"""

from app.app import create_app

from app.libs.error import APIExcption
from app.libs.error_code import ServerError

from werkzeug.exceptions import HTTPException

app = create_app()


# 捕捉全局异常 处理
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIExcption):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIExcption(msg, error_code, code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
