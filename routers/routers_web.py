
""" Модуль с функциями обработки путей для методов API c веб-интерфейсом"""

from time import time

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from functions.app_func import request_to_es, request_to_psql
from functions.app_func import delete_post_es, delete_post_psql


templates = Jinja2Templates(directory='templates')

router_web = APIRouter(
    tags=['Web interface']
)


@router_web.get("/")
def start_search_page(request: Request):

    """
        Запрос вызова главной страницы с возможностью выполнения поискового запроса.

            :return: При вводе запроса и выполнении поиска, перенаправит по маршруту "/search/{search_request}"
                     Если запрос для поиска не введен, при попытке выполнения перенаправит по маршруту "/search"
    """

    return templates.TemplateResponse('start_page.html', {"request": request})


@router_web.get("/search")
@router_web.get("/delete")
def search_or_delete_page(request: Request):

    """
        Попытка выполнения поиска или удаления постов без введенного запроса приводит к перенаправлению
        на данный маршрут для повторной попытки ввода и выполнения запроса.

            :return: При вводе запроса и выполнении поиска, перенаправит по маршруту "/search/{search_request}"
                     Если запрос для поиска не введен, при попытке выполнения перенаправит по маршруту "/search"

                     При вводе запроса и выполнении удаления, перенаправит по маршруту "/delete/{post_id}"
                     Если запрос для удаления не введен, при попытке выполнения перенаправит по маршруту "/delete""
    """

    posts = ["Какой запрос - такой ответ!)"]

    return templates.TemplateResponse('search_results.html', {"request": request, "posts": posts})


@router_web.get("/search/{search_request}")
def search_results_page(request: Request, search_request: str):

    """
        Запрос позволяет получить данные из БД, соответствующие поисковому запросу.

            :param search_request: Поисковый текстовый запрос.

            :return: Результаты поиска с выгрузкой в HTML-формате на веб-страницу.
    """

    stat_time = time()

    list_id = request_to_es(search_request)

    posts = request_to_psql(list_id)

    response_text = f'Текущие результаты поиска по запросу: " {search_request} "'
    posts.insert(0, response_text)

    search_time = time() - stat_time
    posts.insert(1, search_time)

    if len(posts) > 2:

        return templates.TemplateResponse('search_results.html', {"request": request, "posts": posts})

    else:

        response_text = f'По текущему запросу " {search_request} " ничего не найдено.'
        posts.insert(0, response_text)

        search_time = time() - stat_time
        posts.insert(1, search_time)

        return templates.TemplateResponse('search_results.html', {"request": request, "posts": posts[:2]})


@router_web.get("/delete/{post_id}")
def delete_results_page(request: Request, post_id: str):

    """
        Запрос удаляет пост из индекса ElasticSearch и таблицы БД PostgreSQL
        по указанному в параметре запроса "post_id" идентификатору "ID публикации".

            :param post_id: "ID публикации".

            :return: Информационное сообщение о результате с выгрузкой в HTML-формате на веб-страницу.
    """

    response_list = []

    stat_time = time()

    del_time = 0

    try:
        if post_id.isdigit():

            post_id = int(post_id)

            try:

                text_resp_es = delete_post_es(post_id)
                response_list.append(text_resp_es)

                text_resp_psql = delete_post_psql(post_id)
                response_list.append(text_resp_psql)

                del_time = time() - stat_time

            except IndexError:

                response_text = f'Пост с ID: " {post_id} " не найден.'

                response_list.append(response_text)

                del_time = time() - stat_time

        else:

            response_text = "ID поста должен быть числом."

            response_list.append(response_text)

            del_time = time() - stat_time

            raise Exception("Validation Error: Value must be an integer.")

    finally:
        return templates.TemplateResponse('delete_results.html', {"request": request,
                                                                  "resp_list": [del_time, *response_list]})



