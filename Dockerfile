FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app
COPY ./backend.py /app
COPY ./test_main.py /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python backend.py
