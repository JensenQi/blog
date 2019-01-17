# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, String, DateTime, Text
from sqlalchemy.dialects.mysql import LONGTEXT

BaseModel = declarative_base()
