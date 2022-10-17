FROM python:3.10-slim-buster

WORKDIR /app

RUN pip3 install -U pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-w", "1", "-b", ":5000", "app.wsgi:application"]
