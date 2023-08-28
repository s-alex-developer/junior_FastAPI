
""" Глобальные переменные, полученные из файла с переменными окружения '.env' """

import os
from dotenv import load_dotenv

load_dotenv()

ES_HOST = os.getenv("ES_HOST")
ES_PORT = os.getenv("ES_PORT")
ES_INDEX = os.getenv("ES_INDEX")

ES_URL = f"http://{ES_HOST}:{ES_PORT}"


DB = os.getenv("DB")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DNS_URL = f"{DB}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DATA_FILE_PATH = os.getenv("DATA_FILE_PATH")

