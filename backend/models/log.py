# -*- coding: utf-8 -*-
from .base import BaseModel, Column, Integer, String, DateTime


class Log(BaseModel):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, comment=u'日志ID')
    ip = Column(String(16), comment=u'访问ID')
    url = Column(String(256), comment=u'访问路径')
    create_time = Column(DateTime, comment=u'创建时间')

    def __repr__(self):
        return "{}\t{}\t{}\t{}".format(self.id, self.ip, self.url, self.create_time)
