"""
    Created by Amirk on 2018-07-21.
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.model.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    __password = Column('password', String(100))

    @property
    def passwrord(self):
        return self.__password

    @passwrord.setter
    def password(self, raw):
        self.__password = generate_password_hash(raw)

    @staticmethod
    def register_user_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)
