"""
    Created by Amirk on 2018-07-20.
"""

from flask import Flask


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 注册蓝图
    register_blueprint(app)
    return app
