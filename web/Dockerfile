FROM python:latest

RUN apt-get update

RUN mkdir /web
WORKDIR /web
COPY . /web/

RUN pip install -U pip
RUN pip install -Ur requirements.txt