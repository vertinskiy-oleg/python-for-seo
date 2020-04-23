import random
from requests_html import HTMLSession
from db_olx import Category, Ad
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


class OlxParser:

    def __init__(self):
        self.start_url = 'https://www.olx.ua/'
        self.category_xpath = '//li/a[@data-id]/@href'
        self.proxies = []
        self.agents = []
        self.session = HTMLSession()
        self.set_all_agents()
        self.url_q = Queue()

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
        for link in links:
            self.url_q.put(link)

    def parser(self):

        while self.url_q.qsize() > 0:

            link = self.url_q.get()

            category = Category.create(name=link)

            headers = self.get_random_headers()
            response = self.session.get(link, headers=headers)

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

                except IndexError:
                    print('Parse error')

                Ad.create(**ad_data)

            print(f'{link} scanned')

    def main(self):
        self.get_category_links()
        threads = 4
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for _ in range(threads):
                executor.submit(self.parser)


if __name__ == '__main__':
    olx = OlxParser()
    olx.main()
