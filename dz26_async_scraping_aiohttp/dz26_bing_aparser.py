import random
import asyncio
from requests_html import AsyncHTMLSession
from db import KeyResults, objects


with open('keywords.txt', 'r', encoding='utf-8') as f:
    KEYS = [line.strip() for line in f]


async def worker():
    asession = AsyncHTMLSession()
    while len(KEYS) != 0:
        key = KEYS.pop(0)
        url = f'https://www.bing.com/search?q={key}&count=50'
        try:
            resp = await asession.get(url)

        except Exception as e:
            print(e, type(e))
            continue

        try:
            snippets = resp.html.xpath('//li[@class="b_algo"]')
        except IndexError:
            snippets = 'Not Found'


        for n, snippet in enumerate(snippets, start=1):
            try:
                href = snippet.xpath('//h2/a/@href')[0]
            except Exception as e:
                print('href error', e)
                continue
            try:
                title = snippet.xpath('//h2')[0].text
            except Exception as e:
                print('title error', e)
                continue
            try:
                description = snippet.xpath('//div[@class="b_caption"]/p')[0].text
            except Exception as e:
                print('description error', e)
                continue

            position = n

            key_results = {"key": key, "url": href, "title": title, 
                            "description": description, "position": position}

            await objects.create(KeyResults, **key_results)

        print('OK', key)


async def main():
    num_cor = 5
    tasks = []
    for _ in range(num_cor):
        tasks.append(worker())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
