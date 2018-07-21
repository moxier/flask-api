"""
    Created by Amirk on 2018-07-21.
"""

from enum import Enum

# 枚举
class ClintTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
