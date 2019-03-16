# Django-Eventops-BoilerPlate

Django with docker setup used for staging and production environments. 2 docker containers are maintanined. One with django, gunicorn and supervisord and the other with nginx.

Functionalities materialized are:
  Database switching based on request using db router and middleware
  Django dockerization
  Environment variables set for docker env
