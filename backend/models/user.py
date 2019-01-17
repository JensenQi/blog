# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin
from sqlalchemy import Column, Integer, Text, String
from werkzeug.security import generate_password_hash, check_password_hash
from .base import BaseModel


class User(UserMixin, BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, comment=u"用户ID")
    user_name = Column(String(16), comment=u'账号')
    password_hash = Column(String(128), comment=u"密码")

    @property
    def password(self):
        raise AttributeError('password只读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return self.id
