# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster as base

COPY . /app/
WORKDIR /app/

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

RUN pip install --upgrade pip setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

FROM base as dev
ENV FLASK_ENV=development
CMD flask run

FROM base as testing
ENV FLASK_ENV=testing
CMD cd tests && python -m pytest

FROM base as production
ENV FLASK_ENV=production
CMD gunicorn -w 4 -b 0.0.0.0:5000 app:app
