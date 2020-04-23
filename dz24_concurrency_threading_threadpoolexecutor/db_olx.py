from peewee import *

connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = PostgresqlDatabase('library', autorollback=True, **connection)


class Category(Model):
    name = TextField()

    class Meta:
        database = db
        table_name = 'VertinskyiOlxCategory_24'


class Ad(Model):
    title = TextField()
    date = TextField()
    price = TextField()
    photo = TextField()
    link = TextField()
    city = TextField()
    category = ForeignKeyField(VertinskyiOlxCategory_24, backref='ads')

    class Meta:
        database = db
        table_name = 'VertinskyiOlxAd_24'


if __name__ == '__main__':
    db.drop_tables([VertinskyiOlxCategory_24, VertinskyiOlxAd_24])
    db.create_tables([VertinskyiOlxCategory_24, VertinskyiOlxAd_24])
