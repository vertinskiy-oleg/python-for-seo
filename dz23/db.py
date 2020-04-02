from peewee import *

connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = PostgresqlDatabase('library', autorollback=True, **connection)


class VertinskyiOlehOlxCategory(Model):
    name = TextField()

    class Meta:
        database = db


class VertinskyiOlehOlxAd(Model):
    title = TextField()
    date = TextField()
    price = TextField()
    photo = TextField()
    link = TextField()
    city = TextField()
    category = ForeignKeyField(VertinskyiOlehOlxCategory, backref='ads')

    class Meta:
        database = db


if __name__ == '__main__':
    db.drop_tables([VertinskyiOlehOlxCategory, VertinskyiOlehOlxAd])
    db.create_tables([VertinskyiOlehOlxCategory, VertinskyiOlehOlxAd])
