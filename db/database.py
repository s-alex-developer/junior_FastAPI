
"""
    Модуль содержит основные Объекты и Классы для взаимодействия с БД PostgreSQL и индексом ElasticSearch.

"""

import sys

sys.path.append('..')

from sqlalchemy import create_engine
from elasticsearch import Elasticsearch
from sqlalchemy.orm import declarative_base, sessionmaker

from settings.global_var import DNS_URL, ES_URL


Base = declarative_base()

DNS = DNS_URL
engine = create_engine(DNS)

SessionLocal = sessionmaker(bind=engine)

es = Elasticsearch(ES_URL)
