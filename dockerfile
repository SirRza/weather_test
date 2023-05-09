#syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /test_docker

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "run.py"]