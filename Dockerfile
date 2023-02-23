# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

MAINTAINER Stanislav Zoldak szoldak28@gmail.com

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=django_exercise.settings
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]