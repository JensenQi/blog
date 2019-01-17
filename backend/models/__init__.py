# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URI, ROOT_NAME, ROOT_PASSWD
from .base import BaseModel
from .user import User
from .article import Article
from .log import Log

engine = create_engine(DB_URI, pool_recycle=3600, encoding='utf-8')
DBSession = sessionmaker(engine)


def build_db():
    BaseModel.metadata.create_all(engine)
    root = User()
    root.user_name = ROOT_NAME
    root.password = ROOT_PASSWD
    session = DBSession()
    session.add(root)
    session.commit()
    session.close()


def reset_db():
    BaseModel.metadata.drop_all(engine)
    build_db()
