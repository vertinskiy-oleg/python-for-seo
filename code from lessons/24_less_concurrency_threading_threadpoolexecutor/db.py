import datetime
from peewee import *


connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = PostgresqlDatabase('library', autorollback=True, **connection)


class Page(Model):
    title = CharField(max_length=1024, index=True)
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'pages_24'


if __name__ == '__main__':
    db.drop_tables([Page])
    db.create_tables([Page])
