FROM python:3.9

RUN pip install flask sqlalchemy

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]