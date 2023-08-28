
"""
    Модуль для создания таблицы БД PostgreSQL и индекса в ElasticSearch.

        1. Запуск модуля создает таблицу и индекс, наполняет их исходными данными из файла "posts.csv"
        при помощи функции load_to_db().

        2. Функция delete_db() - удаляет индекс и таблицу со всеми данными.
"""

import csv
import sys

sys.path.append('..')

from tqdm import tqdm
from db.models import Posts
from settings.global_var import ES_INDEX, DATA_FILE_PATH, DB_NAME, DB
from db.database import SessionLocal, Base, engine, es


def load_to_db(data_file_path: str):

    """
        Функция наполняет индекс и таблицу БД данными из файла.

            :param data_file_path : Путь к файлу.
            :return: None
    """
    session = SessionLocal()

    try:
        current_db_row_id = 1

        with open(data_file_path) as file:
            posts = csv.DictReader(file)

            for post in tqdm(posts):
                current_db_row = Posts(id=current_db_row_id, rubrics=post['rubrics'], text=post['text'],
                                       created_date=post['created_date'])

                session.add(current_db_row)
                session.commit()

                doc = {
                    'id': current_db_row_id,
                    'text': post['text'],
                }

                es.index(index=ES_INDEX, document=doc)

                current_db_row_id += 1

    finally:
        session.close()


def delete_db():

    """
        Функция удаляет индекс и таблицу БД со всеми данными.

            :return: None
    """
    es.indices.delete(index=ES_INDEX)

    Base.metadata.drop_all(engine)

    print(f'\nИндекс "{ES_INDEX}" удален из ElasticSearch.')
    print(f'Таблица "{Posts.__tablename__}" удалена из БД {DB} "{DB_NAME}".')


if __name__ == "__main__":

    es.indices.create(index=ES_INDEX)
    print(f'\nИндекс "{ES_INDEX}" создан в ElasticSearch.')

    Base.metadata.create_all(engine)
    print(f'Таблица "{Posts.__tablename__}" создана в БД {DB} "{DB_NAME}".')

    print(f'\nНачинается загрузка данных в индекс "{ES_INDEX}" и таблицу "{Posts.__tablename__}".')
    print(f'Относительный путь к файлу с данными "{DATA_FILE_PATH}".')

    load_to_db(DATA_FILE_PATH)

    print("\nЗагрузка данных завершена.")


