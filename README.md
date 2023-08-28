## `ЗАДАНИЕ:`
<details>
    <summary>Тестовое задание для стажера Python ...</summary>

Необходимо написать очень простой поисковик по текстам документов. Данные хранятся в БД по желанию (кроме sqlite), поисковый индекс в эластике. 

Ссылка на тестовый массив данных: [[csv](https://github.com/s-alex-developer/junior_FastAPI/blob/main/temp/posts.csv)]

### Структура БД:

- `id` - уникальный для каждого документа;
- `rubrics` - массив рубрик;
- `text` - текст документа;
- `created_date` - дата создания документа.

### Структура Индекса:

- `iD` - id из базы;
- `text` - текст из структуры БД.

### Необходимые методы

- сервис должен принимать на вход произвольный текстовый запрос, искать по тексту документа в индексе и возвращать первые 20 документов со всем полями БД, упорядоченные по дате создания;
- удалять документ из БД и индекса по полю  `id`.

### Технические требования:

- любой python фреймворк кроме Django и DRF;
- `README` с гайдом по поднятию;
- `docs.json` - документация к сервису в формате openapi.

### Программа максимум:

- функциональные тесты;
- сервис работает в Docker;
- асинхронные вызовы.

</details>

***

### Примечание:
Поскольку в задании четких требований к обработке и работе с поисковым запросом не указано, были использованы:
1. В качестве **термина-запроса** `"match_phrase"` с параметром `"slop": 0`, то есть будет производится поиск в тексте документа всей фразы с соблюдением порядка слов. Наличие посторонних слов между словами запроса не допускается.

2. Стандартные настройки (по умолчанию) для **анализатора** и оценки **релевантности**.

## `ТЕХНОЛОГИИ И ИНСТРУМЕНТЫ:`

<img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/python.svg" width="18" height="18"> [**Python**](https://www.python.org/) \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/fastapi.svg" width="18" height="18"> [**FastAPI**](https://fastapi.tiangolo.com/) \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/jinja.svg" width="18" height="18"> [**jinja2**](https://jinja.palletsprojects.com/en/3.1.x/)


<img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/postgresql.svg" width="18" height="18"> [**PostgreSQL**](https://www.postgresql.org/)  \  <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/elasticsearch.svg" width="18" height="18"> [**ElasticSearch**](https://www.elastic.co/elasticsearch/) \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/kibana.svg" width="18" height="18"> [**Kibana**](https://www.elastic.co/kibana)

<img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/pycharm.svg" width="18" height="18"> [**PyCharm**](https://www.jetbrains.com/ru-ru/pycharm/) \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/git.svg" width="18" height="18"> [**Git**](https://git-scm.com/) \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/github.svg" width="18" height="18"> **GitHub** \ <img src="https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/icon/docker.svg" width="18" height="18"> [**Docker**](https://www.docker.com/)

## `СТРУКТУРА ПРОЕКТА:`

<details>
    <summary>Показать \ Скрыть >>></summary>


```
junior_FastAPI
├── db/
│   ├── crud.py
│   ├── database.py
│   ├── del.py
│   └── models.py
│
├── functions/
│   └── app_func.py
│
├── routers/
│   ├── routers_api.py
│   └── routers_web.py
│
├── settings/
│   └── global_var.py
│
├── temp/
│   └── posts.csv
│
├── templates/
│   ├── base.html
│   ├── delete_results.html
│   ├── search_results.html
│   └── start_page.html
│
├── docker-compose.yml
├── Dockerfile
├── docs.json
├── main.py
├── README.md
└── requirements.txt
```

</details>

## `ГАЙД ПО ПОДНЯТИЮ:`
### 1. Запуск в среде Docker (оптимальный вариант).

**Требования:**

* Установлен **Docker** (обязательно)
* Установлена **Git** (опционально)

<details>
    <summary>Показать \ Скрыть >>></summary>
    

    
### 1. Скачиваем файлы проекта:
***    
* Используем возможности **Git** и **GitHub**:
  * Выбираем каталог для сохранения файлов.
  * Запускаем **Git Bash** и выполняем клонирование репозитория.
  * Используем команду: `git clone git@github.com:s-alex-developer/junior_FastAPI.git`
  
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/1.png)


* Так же файлы проекта можно скачать в виде архива:

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/2.png)


### 2. Скачиваем файл с переменными окружения [ [.env](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/.env) ] и добавляем его в корневой каталог проекта.**:
***   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/3.png)


### 3. Запускаем приложение **Docker Desktop** и открываем вкладку **Images**:
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/4.png)


### 4. Копируем путь к проекту и открываем командную строку:
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/5.png)


### 5. Переходим в корневую директорию проекта, в которой находится файл `docker-compose.yml` и выполняем команду: `docker compose up -d` :
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/6.png)


### 6. Ожидаем пока все необходимые образы будут скачены и завершится процесс создания и запуска контейнеров, с установкой всех зависимостей и настройкой внутренней сети:
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/7.png)


### 7. Возвращаемся в **Docker Desktop** и проверяем вкладку **Images**:

***
* Все отмеченные образы должны быть загружены и находится в статусе `In use`:

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/8.png)


### 8. Переходим во вкладку **Containers** и проверяем состояние контейнеров, созданных и запущенных из наших образов:
***
* Все отмеченные контейнеры должны быть запущены, о чем свидетельствует статус `Running` 

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/9.png)


### 9. Далее нам необходимо создать таблицу БД и индекс в ElasticSearch и наполнить их данными:
***

* Выполним следующий порядок действий:

  
    * Выведем информацию о запущенных в данный момент контейнерах, выполнив команду: `docker ps`


    * Нас интересует контейнер `my_app_image`, запустим дополнительный процесс в данном контейнере, 
   используя **CONTAINER ID** и команду: `docker exec -it 5d2f3c06264e bash`
    * Когда дополнительный процесс в виде оболочки командной строки `bash` запущен 
   (в интерактивном режиме терминала `-it`), мы можем добраться до файла `crud.py`, 
   запуск которого создаст таблицу в БД, индекс в ElasticSearch 
   и наполнит их тестовыми данными из файла `posts.csv`
    * Из каталога с файлом `crud.py` выполняем команду `python crud.py` и ждем сообщения о завершении 
   процесса:
   
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/10.png)
      
    * Выполнение команды `python del.py`, в том же каталоге, приведет к удалению таблицы из БД, индекса из ElasticSearch и всех загруженных данных. 

### 10. Возвращаемся в **Docker Desktop** во вкладку **Containers**:
***
* Нас интересует контейнеры `my_elasticsearch` и `my_app_image`
* Благодаря настроенному маппингу портов мы можем подключиться к нашим контейнерам (приложениям) из внешней среды, например через браузер.
* Нажимаем на ссылку с портами (см. скрин ниже) и проверим работоспособность **ElasticSearch**:
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/ES.png)

* Если приложение **ElasticSearch** запущено корректно по адресу `localhost:9292` мы должны увидеть страницу примерного содержания: 
      
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/ES1.png)

* По тому же принципу, перейдя по адресу `localhost:8008` или нажав на ссылку с портами мы попадём на главную страницу нашего приложения:
    
   ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/11.png)


### 11. Работа с приложением:
***
* Вводим поисковый запрос:

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/12.png)

* Получаем результат из БД, в виде странного поста от не менее странного молодого человека : )

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/13.png)
    
* Используем 'ID публикации' удаляем это шедевр из **таблицы БД** и индекса **ElasticSearch**, о чем нам с радостью сообщает приложение:
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/14.png)
    
* Попытка ввести удаленный или несуществующий 'ID публикации' сопровождается сообщением:
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/15.png)

* Так же, как и попытка ввода различных сущностей не похожих на цифры:

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/16.png)
    
* Попытка поиска или удаления с пустыми значениями полей приводит к ответу:

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/17.png)

* Если приложению не удается найти данные соответствующие поисковому запросу, результат будет следующим:
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/18.png)
    
### 12. Документация при текущих настройках портов будет доступна по адресу `localhost:8008/docs`
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/19.png)


### 13. Дополнительные инструменты и возможности:
***
* Для удобства взаимодействия с **PostgreSQL** добавлено приложение **PgAdmin** доступное по адресу `localhost:8080`
  
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/20.png)

  * Как подключится:
    * **Login:** `junior@gmail.com`
    * **password:** `junior`
      
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/21.png)
      
    * **Имя:** `junior_db`

        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/22.png)
      
    * **Имя/адрес сервера:** `postgres`
    * **Имя пользователя:** `junior`
    * **Пароль:** `junior`
      
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/23.png)

    * После подключения, находим нашу таблицу и для проверки выполняем запрос выводящий все данные:

        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/24.png)
    
    * Получаем результат:
    
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/25.png)

  * Для работы с индексами **ElasticSearch** добавлено приложение **Kibana** доступное по адресу `localhost:5656`
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/26.png)
    
    * С главной страницы переходим в раздел **Dev Tools**:
      
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/27.png)
      
    * Используя запросы, мы можем получать различную информацию об индексе и хранящихся там данных, что может пригодиться для проверки результатов поиска нашего приложения: 
        
        ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/28.png)
        
**Запросы, которые могут пригодиться во время проверки:**
```
# Информация по индексам:

GET _cat/indices


#Запрос соответствия фразе (когда важен порядок слов) с параметром "slop".
#Параметр "slop" позволяет задать количество слов, которые могу находится между словами основного выражения поиска.

GET junior/_search
{"from" : 0, 
 "size" : 30, 
 "query": {
    "match_phrase": {
      "text": {
        "query": "Программист", 
        "slop": 0
      }
    }
  }
}

# Удалить индекс:

DELETE junior
```

### 14. Завершение работы.
***
* После завершения работы с приложением контейнеры необходимо остановить и при необходимости удалить:
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/29.png)
    
* Так же можно удалить созданный образ нашего приложения и образы других приложений, если дальнейшее их использование не планируется.
    
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/30.png)

***  

</details>

### 2. Запуск в среде ОС (на примере Windows).

**Требования:**
* Установлен **Python** (обязательно)
* Установлена **IDE** (в нашем случае **PyCharm**)
* Установлена **PostgreSQL** (обязательно)
* Установлен **ElasticSearch** (обязательно)
* Установлена **Git** (опционально)

<details>
    <summary>Показать \ Скрыть >>></summary>
    
### 1. Скачиваем файлы проекта:
***    
* Используем возможности **Git** и **GitHub**:
  * Выбираем каталог для сохранения файлов.
  * Запускаем **Git Bash** и выполняем клонирование репозитория.
  * Используем команду: `git clone git@github.com:s-alex-developer/junior_FastAPI.git`
  
    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/1.png)


* Так же файлы проекта можно скачать в виде архива:

    ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/2.png)

### 2. Открываем как проект `PyCharm`:
***    
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/1.png)

### 3. Внутри проект `PyCharm` создаем и активируем виртуальное окружение:
***    
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/2.png)

### 4. Устанавливаем виртуальное окружение из файла `requirements.txt` и при необходимости обновляем менеджер пакетов `pip`:
***    
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/3.png)

### 5. Далее необходимо создать БД (в нашем случае использована СУБД PostgreSQL):
***
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/4.png)
* Где `postgres` - имя пользователя **СУБД PostgreSQL**, а `juniordb` - имя базы данных.

### 6. Запускаем `ElasticSearch`, установленный на компьютере:
***  
* Если приложение **ElasticSearch** запущено корректно по адресу `localhost:9200` мы должны увидеть страницу примерного содержания:
  
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/5.png)

### 7. Скачиваем файл с переменными окружения [ [.env](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/.env) ] и добавляем его в корневой каталог проекта:
***
* Файл имеет следующую структуру и набор данных, которые будет необхдимо дополнить:
```python
ES_HOST=localhost  # По умолчанию.
ES_PORT=9200       # По умолчанию.
ES_INDEX=          # Название индекса в ElasticSearch.

DB=postgresql      # Используемая СУБД (в нашем проекте это PostrgeSQL).
DB_USER=           # Имя пользователя СУБД.
DB_PASS=           # Пароль пользователя СУБД.
DB_HOST=localhost  # По умолчанию.
DB_PORT=5432       # По умолчанию.
DB_NAME=           # Имя базы данных.

DATA_FILE_PATH=../temp/posts.csv  # Путь к файлу с тестовыми данными.
```

### 8. Запустим наше приложение через командную строку в `IDE PyCharm`:
***
* Выполнения команды `uvicorn main:app` должно производится из директории проекта, где расположен файл **main.py**

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/6.png)

### 9. Создаем таблицу БД, индекс в `ElasticSearch` и наполняем тестовыми данными:
***
* Выполняем последовательность команд для перехода в каталог `db` и запуска модуля `crud.py`

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/7.png)

### 10. Приложение запущено и готово к работе:
***
* Главная страница доступна по адресу `localhost:8000`

  ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/8.png)

* Документация по адресу `localhost:8000/docs`

  ![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/junior_FastAPI/OS/9.png)

***
