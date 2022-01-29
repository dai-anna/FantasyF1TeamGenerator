FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app
COPY ./backend.py /app
COPY ./test_all.py /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "backend.py"]
