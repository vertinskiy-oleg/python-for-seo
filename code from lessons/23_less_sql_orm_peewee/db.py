from peewee import PostgresqlDatabase, Model, CharField, TextField


connection = {
    'user': 'py4seo',
    'password': 'PY1111forSEO',
    'host': '46.30.164.249',
    'port': 5432
}


db = PostgresqlDatabase('library', **connection)


class MyTexts(Model):
    key = CharField()
    slug = CharField()
    text = TextField()

    class Meta:
        database = db
        table_name = 'dor_texts'


# sql = "INSERT INTO dor_texts VALUES (556, 'value2', 'value3', 'Hello World');"
# db.execute_sql(sql)

# cursor = db.execute_sql('select * from dor_texts where slug = "asterisk";')
# for raw in cursor:
#     print(raw)

# text = MyTexts.create(
#     key='blabla',
#     slug='asdasdasdadsasd',
#     text="""asdasdasd'asdasdasdas"Asdasdasdasdasd\n"""
# )
# print(text)

# all_texts = MyTexts.select().where(MyTexts.slug == 'asterisk')
# for txt in all_texts:
#     print(txt.key, txt.slug)



