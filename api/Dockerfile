FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV REGISTRY_VALIDATION_DISABLED=true
# install dependencies
RUN python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app/api/
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/api/

#EXPOSE 5001
#RUN gunicorn -b 0.0.0.0:8080 wsgi
#RUN python wsgi.py upgrade
#ENV FLASK_APP=wsgi.py
#RUN flask db upgrade
