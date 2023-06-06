FROM python:3.11

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend_app

COPY ./requirements.txt /backend_app/

RUN pip install -r requirements.txt

COPY ./api_server /backend_app/