# syntax=docker/dockerfile:1
FROM ubuntu
ENV PYTHONUNBUFFERED=1
ENV TZ=Europe/Samara
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update

RUN apt-get install -y apt-utils apache2 vim curl apache2-utils python3 libapache2-mod-wsgi-py3 python3-pip
RUN pip install --upgrade pip 
WORKDIR /code
COPY docker/requirements.txt /code/
RUN pip install -r requirements.txt

COPY src/ /code/
COPY docker/site-config.conf /etc/apache2/sites-available/000-default.conf
COPY docker/apache2.conf /etc/apache2/apache2.conf

RUN chown :www-data /code/logs

EXPOSE 80
#ENTRYPOINT /bin/bash
ENTRYPOINT apache2ctl -D FOREGROUND
#python manage.py runserver 0.0.0.0:3000
