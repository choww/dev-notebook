FROM python:3.10.3-alpine

RUN apk add --update postgresql-dev nodejs npm 

COPY . .

RUN pip3 install -r requirements.txt \
  && npm ci && \
  python3 app/manage.py makemigrations && \
  python3 app/manage.py migrate

WORKDIR app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
