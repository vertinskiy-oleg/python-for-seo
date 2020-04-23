import datetime
from requests_html import HTMLSession
from peewee import DoesNotExist
from db2 import Keyword, Page, Category, PageKeywords


my_keys = [
    'buy laptop',
    'buy xiaomi',
    'buy iphone',
    # 'buy samsung'
]


def google_craper(keyword, category_id, lang='en', serp_count=10):

    try:

        db_key = Keyword.get(name=keyword)
        db_key.updated = datetime.datetime.now()
        db_key.save()

    except DoesNotExist:
        db_key = Keyword.create(
            name=keyword,
            updated=datetime.datetime.now(),
            category_id=category_id
        )

    session = HTMLSession()

    resp = session.get(
        f'https://www.google.com/search?q={db_key.name}&num={serp_count}&hl={lang}')

    snipets = resp.html.xpath('//div[@class="g"]')

    db_pages = []

    for sn in snipets:
        title = sn.xpath('//h3')[0].text
        description = sn.xpath('//span[@class="st"]')[0].text
        url = sn.xpath('//div[@class="r"]/a[1]/@href')[0]

        data = {
            'title': title,
            'description': description,
            'url': url
        }

        db_pages.append(data)

        # try:
        #
        #     page_id = Page.create(**data)
        #     db_key.pages.add(Page.get(Page.id == page_id))
        #     print(page_id, url)
        #
        # except Exception as e:
        #     print(e, type(e), url)

    Page.insert_many(db_pages).execute()


def main():
    try:
        category = Category.get(name='ecommerce')

    except DoesNotExist:
        category = Category.create(
            name='ecommerce',
            description='ecommerce category'
        )

    PageKeywords.delete().execute()
    Page.delete().execute()

    for key in my_keys:
        google_craper(key, category)


if __name__ == '__main__':
    main()
