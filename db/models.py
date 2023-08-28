
"""
    Модуль содержащий класс Posts - модель, описывающую таблицу "posts" в БД PostgreSQL.
"""


from db.database import Base

from sqlalchemy import Column, Integer, VARCHAR, Text, DateTime


class Posts(Base):

    """
        Модель, описывающая таблицу "posts" в БД PostgreSQL.
    """

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    rubrics = Column(VARCHAR(100))
    text = Column(Text)
    created_date = Column(DateTime)

    def __str__(self):
        return f"id: {self.id}, rubrics: {self.rubrics}, created_date: {self.created_date}, text: {self.text}"
