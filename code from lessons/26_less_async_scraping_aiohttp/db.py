import datetime
import peewee_async
from peewee import *


connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = peewee_async.PostgresqlDatabase('library', autorollback=True, **connection)


class Page(Model):
    title = CharField(max_length=1024, index=True)
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'pages_26'


objects = peewee_async.Manager(db)


if __name__ == '__main__':
    db.drop_tables([Page])
    db.create_tables([Page])
