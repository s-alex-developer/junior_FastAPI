
"""
    Модуль содержит функции взаимодействия с таблицей БД PostgreSQL и индексом в ElasticSearch.
"""


from db.models import Posts
from db.database import SessionLocal, es
from settings.global_var import ES_INDEX


def request_to_es(request_text: str) -> list[int]:

    """
        Функция производит поисковый запрос в индекс ElasticSearch.

            :param request_text: Поисковый запрос от пользователя в ElasticSearch.
            :return: Список, содержащий id постов, наиболее точно соответствующих поисковому запросу.
    """

    query = {
        "from": 0,
        "size": 20,
        "query": {
            "match_phrase": {
                "text": {
                    "query": request_text,
                    "slop": 0  # Если захотим сделать наш запрос немного Elastich'ней)
                }
            }
        }
    }

    resp = es.search(index=ES_INDEX, body=query)

    id_list = []

    for el in resp['hits']['hits']:

        id_list.append(el['_source']['id'])

    return id_list


def request_to_psql(id_list: list[int]) -> list:

    """
        Функция производит запрос в таблицу БД PostgreSQL.

            :param id_list: Список, содержащий id записей таблицы БД, которые необходимо получить.
            :return: Список словарей. Каждый словарь содержит все поля и их значения одной записи из таблицы БД.
    """

    session = SessionLocal()

    try:
        results = session.query(Posts).filter(Posts.id.in_(id_list)).order_by(Posts.created_date)

        docs_list = []

        for result in results:

            docs = {"id": result.id, 'rubrics': result.rubrics, 'text': result.text,
                    'created_date': result.created_date}
            docs_list.append(docs)

        return docs_list

    finally:
        session.close()


def delete_post_es(post_id: int) -> str:

    """
        Функция удаляет документ из индекса ElasticSearch.

            :param post_id: Идентификатор поста для удаления.
            :return: Информационное сообщение.
    """

    query = {
        "query": {
            "match": {
                "id": {
                    "query": post_id
                }
            }
        }
    }

    post_id_es = es.search(index=ES_INDEX, body=query)['hits']['hits'][0]['_id']

    es.delete(index=ES_INDEX, id=post_id_es)

    return f'Пост с ID: " {post_id} " успешно удален из ElasticSearch.'


def delete_post_psql(post_id: int) -> str:

    """
        Функция удаляет запись из таблицы БД PostgreSQL.

            :param post_id: Идентификатор записи для удаления.
            :return: Информационное сообщение.
    """

    session = SessionLocal()

    try:
        session.query(Posts).filter(Posts.id == post_id).delete()

        session.commit()

        return f'Пост с ID: " {post_id} " успешно удален из PostgreSQL.'

    finally:
        session.close()
