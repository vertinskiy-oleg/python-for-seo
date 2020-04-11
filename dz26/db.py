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


class KeyResults(Model):
    key = CharField(max_length=255)
    url = CharField(max_length=1024)
    title = CharField(max_length=1024)
    description = CharField(max_length=1024)
    position = IntegerField()
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'vertinskiy_dz26'


objects = peewee_async.Manager(db)


if __name__ == '__main__':
    # db.drop_tables([KeyResults])
    db.create_tables([KeyResults])
