# -*- coding: utf-8 -*-
from .base import BaseModel, Column, Integer, String, LONGTEXT, Boolean, DateTime, Text


class Article(BaseModel):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, comment=u'文章ID')
    title = Column(String(512), comment=u'文章标题')
    abstract = Column(LONGTEXT, comment=u'摘要')
    content = Column(LONGTEXT, comment=u'文章内容')
    more = Column(Boolean, default=False, comment=u'是否产生摘要')
    release = Column(Boolean, default=False, comment=u'是否发布')
    create_time = Column(DateTime, comment=u'创建时间')
    update_time = Column(DateTime, comment=u'更新时间')
    remove = Column(Boolean, default=False, index=True, comment=u'是否删除')

    def __repr__(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.id,
            self.title,
            '已发布' if self.release else '草稿',
            self.create_time,
            self.update_time
        )

    def to_json(self, full_content=True):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content if full_content else self.abstract,
            'more': self.more,
            'release': self.release,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
