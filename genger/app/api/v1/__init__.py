"""
    Created by Amirk on 2018-07-20.
"""
from flask import Blueprint

from app.api.v1 import user, book


def create_blueprint_v1():
    bp_v1 = Blueprint('bp_v1', __name__)

    # 将红图注册到蓝图上
    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')

    return bp_v1