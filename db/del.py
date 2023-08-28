
"""
    Запуск данного модуля вызовет работу функции delete_db() и удаляет индекс ElasticSearch и таблицу БД PostgreSQL
    со всеми данными.
"""

from crud import delete_db

if __name__ == "__main__":
    delete_db()
