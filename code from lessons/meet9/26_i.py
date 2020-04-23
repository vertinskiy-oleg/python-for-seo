import asyncio
import aiohttp
import random
from lxml import html
# from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
# from db import Page, objects

with open('keys.txt', 'r') as f:
    LINKS_QUEUE = set([line.strip() for line in f if line.strip()])

with open('ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]


async def worker():
    async with aiohttp.ClientSession() as session:
        while True:

            if len(LINKS_QUEUE) == 0:
                print('QUEUE ENDED')
                break

            key = LINKS_QUEUE.pop()
#           url = f'https://www.bing.com/search?q={key}'
            url = f'https://www.google.ru/search?q={key}&num=10&hl=ru'

            try:
                # resp = session.get(url)
                print('SEND', url)

                # resp = requests.get(url)
                # html_code = resp.text
                # assert resp.status_code == 200

                rand_headers = {'User-Agent': random.choice(USER_AGENTS)}

                resp = await session.get(url, headers=rand_headers)

                html_code = await resp.text()
#                print(html_code)
                assert resp.status == 200
                print('GET', url)
            except Exception as e:
                print(e, type(e))
                continue

            try:
                dom_tree = html.fromstring(html_code)
                print('Dom_tree OK')
            except ValueError:
                continue

            try:
                url1 = dom_tree.xpath('//div[@class="r"]/a/@href')[0]
                url2 = dom_tree.xpath('//div[@class="r"]/a/@href')[1]
                url3 = dom_tree.xpath('//div[@class="r"]/a/@href')[2]
                url4 = dom_tree.xpath('//div[@class="r"]/a/@href')[3]
                url5 = dom_tree.xpath('//div[@class="r"]/a/@href')[4]
#                url1 = dom_tree.xpath('//li[@class="b_algo"]/h2/a/@href')
                print('URL1 = ', url1, url2, url3, url4, url5)
            except IndexError:
                print('Not Found')
                url1 = url2 = url3 = url4 = url5 = 'Not Found'

            page = {"url1": url1, "url2": url2, "url3": url3, "url4": url4, "url5": url5,  "key": key}
            # await objects.create(Page, **page)

            print('OK', page)


async def main():
    key = 'продвижение сайтов'
    LINKS_QUEUE.add(key)

    thread = 5
    tasks = []
    for _ in range(thread):
        tasks.append(worker())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())