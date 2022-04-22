FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./backend.py /app
COPY ./test_all.py /app

EXPOSE 8080

CMD ["python", "backend.py"]
