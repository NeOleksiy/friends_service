# Стартовый образ
FROM python:3.11.2

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY . /project/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

