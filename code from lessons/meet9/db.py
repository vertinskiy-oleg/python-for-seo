import datetime
from time import sleep
import peewee_async
from peewee import *


connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = PostgresqlDatabase('library', **connection)


class Page(Model):
    title2 = CharField(max_length=1024, index=True)
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = '26_v'

# objects = peewee_async.Manager(db)


if __name__ == '__main__':

    if Page._meta.table_name in db.get_tables():
        db.drop_tables([Page], safe=True, cascade=True)

    db.create_tables([Page])
