FROM python:3

MAINTAINER Silvio Sampaio <silviocs@imd.ufrn.br>

# Install hug api & app

COPY app /usr/src/app

RUN pip3 install -r /usr/src/app/requirements.txt

CMD hug -f /usr/src/app/exemplo.py

EXPOSE 8000

