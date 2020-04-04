import random
from requests_html import HTMLSession
from db import Category, Ad
from peewee import DoesNotExist


class OlxParser:

    def __init__(self):
        self.start_url = 'https://www.olx.ua/'
        self.category_xpath = '//li/a[@data-id]/@href'
        self.proxies = []
        self.agents = []
        self.session = HTMLSession()
        self.set_all_agents()

        print('Crawler Initialized')

    def set_all_agents(self):
        with open('ua.txt', 'r', encoding='utf-8') as f:
            self.agents = [x.strip() for x in f if x.strip()]

    def get_random_headers(self):
        print('get_random_headers')
        return {'User-Agent': random.choice(self.agents)}

    def get_category_links(self):
        headers = self.get_random_headers()
        response = self.session.get(self.start_url, headers=headers)
        links = response.html.xpath(self.category_xpath)
        print('get_category_links', links)
        return links

    def run(self):
        links = self.get_category_links()

        for link in links:
            headers = self.get_random_headers()
            resp = self.session.get(link, headers=headers)
            self.get_ads_and_write_to_db(link, resp)

    def get_ads_and_write_to_db(self, link, response):

        try:
            category = Category.get(name=link)

        except DoesNotExist:
            category = Category.create(
                name=link
            )

        ad_blocks = response.html.xpath('//div[@class="offer-wrapper"]')
        for ad in ad_blocks:
            try:
                ad_title = ad.xpath('//h3')[0].text
                ad_date = ad.xpath('//p[@class="lheight16"]/small[2]')[0].text
                ad_price = ad.xpath('//p[@class="price"]')[0].text
                ad_photo = ad.xpath('//img/@src')[0]
                ad_link = ad.xpath('//h3/a/@href')[0]
                ad_city = ad.xpath('//p[@class="lheight16"]/small[1]')[0].text

                ad_data = {
                    'title': ad_title,
                    'date': ad_date,
                    'price': ad_price,
                    'photo': ad_photo,
                    'link': ad_link,
                    'city': ad_city,
                    'category_id': category
                }

            except Exception as e:
                print('Parse error\n', e, type(e))

            try:
                Ad.create(**ad_data)
            except Exception as e:
                print('DB error\n', e, type(e))


if __name__ == '__main__':
    olx = OlxParser()
    olx.run()
