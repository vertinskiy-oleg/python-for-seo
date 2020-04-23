import datetime
from peewee import *


connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}

db = PostgresqlDatabase('library', autorollback=True, **connection)


class Category(Model):
    name = CharField(max_length=55)
    description = CharField(max_length=255)

    class Meta:
        database = db


class Keyword(Model):
    name = CharField(max_length=127)
    updated = DateTimeField(default=datetime.datetime.now)
    category = ForeignKeyField(Category, related_name='keywords')

    class Meta:
        database = db


class Page(Model):
    title = CharField(max_length=1024, index=True)
    description = CharField(max_length=1024)
    url = CharField(max_length=1024)

    keywords = ManyToManyField(Keyword, backref='pages')

    class Meta:
        database = db


PageKeywords = Page.keywords.get_through_model()


if __name__ == '__main__':
    db.drop_tables([Category, Keyword, Page, PageKeywords])
    db.create_tables([Category, Keyword, Page, PageKeywords])
