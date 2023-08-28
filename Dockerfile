FROM python

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .. .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]