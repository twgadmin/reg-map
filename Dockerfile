# syntax=docker/dockerfile:1
FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

CMD ["uwsgi", "--ini", "uwsgi.ini"]