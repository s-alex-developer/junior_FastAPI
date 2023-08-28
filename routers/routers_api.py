
""" Модуль с функциями обработки путей для методов API """

from fastapi import APIRouter

from functions.app_func import request_to_es, request_to_psql
from functions.app_func import delete_post_es, delete_post_psql

router_api = APIRouter(
    tags=['API methods']
)


@router_api.get("/get_posts")
def search_posts(query: str) -> list[dict]:

    """
        Запрос возвращает список постов из БД PostgreSQL
        наиболее соответствующих поисковому запросу "query".

            :param query: Поисковый текстовый запрос.

            :return: Список словарей, где каждый словарь соответствует одной записи в таблице БД и
                     содержит все поля данной записи и их значения.
    """

    list_id = request_to_es(query)
    results = request_to_psql(list_id)

    return results


@router_api.delete("/delete_post")
def delete_post(post_id: int) -> tuple[str, str] | str:

    """
        Запрос удаляет пост из индекса ElasticSearch и таблицы БД PostgreSQL
        по указанному в параметре запроса "post_id" идентификатору "ID публикации".

            :param post_id: "ID публикации".

            :return: Информационное сообщение о результате.
    """

    try:
        text_resp_es = delete_post_es(post_id)
        text_resp_psql = delete_post_psql(post_id)

        return text_resp_es, text_resp_psql

    except IndexError:

        response_text = f"Пост с ID: {post_id} не найден."

        return response_text


