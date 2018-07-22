"""
    Created by Amirk on 2018-07-20.
"""

# 数据库链接字符串 dialect+driver://username:password@host:port/database
# 链接数据库类型
DIALECT = 'mysql'
# python操作数据库使用的驱动
DRIVER = 'cymysql'
# 用户名
USERNAME = 'root'
# 密码
PASSWORD = 'root'
# host是连接数据库的域名
HOST = '127.0.0.1'
# 端口号
PORT = '3306'
# 链接的数据库
DATABASE = 'flask-api'
# 链接字符串
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8". \
    format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = '\x88D\xf09\xa0A\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'
