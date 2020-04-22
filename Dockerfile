FROM python:latest

MAINTAINER Rodrigo da Silva Souza

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "rodrigo_engineer.py"]