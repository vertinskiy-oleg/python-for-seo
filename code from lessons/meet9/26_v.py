import asyncio
import aiohttp
import random
from lxml import html
# from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
from db import Page, objects


# with open('proxies.txt', 'r') as f:
#     PROXIES = [line.strip() for line in f if line.strip()]

with open('ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]

with open('keys.txt', 'r') as f:
    KEYS_LIST = [line.strip() for line in f if line.strip()]


async def worker(domain):
    async with aiohttp.ClientSession() as session:
        while True:
            if len(KEYS_LIST) == 0:
                break
            key = KEYS_LIST.pop()
            requests_key = f'{domain}search?q={key}'

            try:

                print('SEND', requests_key)
                rand_headers = {'User-Agent': random.choice(USER_AGENTS)}
                resp = await session.get(requests_key, ssl=False, headers=rand_headers)
                html_code = await resp.text()

            except (ConnectionError, TimeoutError) as e:
                print(e, type(e))
                KEYS_LIST.append(key)
                continue

            except Exception as e:
                print(e, type(e))
                continue

            try:
                dom_tree = html.fromstring(html_code)
            except ValueError:
                continue

            try:
                urls = dom_tree.xpath('//h2/a/@href')
            except IndexError:
                urls = 'Not Found'

            for position, url in enumerate(urls, 1):
                page = {"key": key, "position": position, "url": url}
                with open('results.csv', 'a') as f:
                    f.write(f'{key}\t{position}\t{url}\n')

                await objects.create(Page, **page)

                print(page)


async def main():
    domain = 'https://www.bing.com/'

    thread = 2
    tasks = []
    for _ in range(thread):
        tasks.append(worker(domain))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
