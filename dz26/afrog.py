import asyncio
import aiohttp
import random
from lxml import html
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
from db import Page, objects


BAD_PARTS = {
    '.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi', '.css',
    '.mp4', '.webm', '.ico', '/static/', '/media/', '/summernote/'
}


LINKS_QUEUE = set()
SCANNED_LINKS = set()


with open('proxies.txt', 'r') as f:
    PROXIES = [line.strip() for line in f if line.strip()]

with open('ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]


async def worker(domain):
    async with aiohttp.ClientSession() as session:
        while True:

            if len(LINKS_QUEUE) == 0:
                await asyncio.sleep(3)
                if len(LINKS_QUEUE) == 0:
                    break
                continue

            url = LINKS_QUEUE.pop()
            SCANNED_LINKS.add(url)

            try:
                # resp = session.get(url)
                print('SEND', url)

                # resp = requests.get(url)
                # html_code = resp.text
                # assert resp.status_code == 200

                rand_headers = {'User-Agent': random.choice(USER_AGENTS)}
                random_ip = random.choice(PROXIES)
                # connector = ProxyConnector.from_url(f'socks5://{random_ip}')

                resp = await session.get(url, headers=rand_headers)

                html_code = await resp.text()
                assert resp.status == 200

            except Exception as e:
                print(e, type(e))
                continue

            try:
                dom_tree = html.fromstring(html_code)
                dom_tree.make_links_absolute(url, resolve_base_href=True)
            except ValueError:
                continue

            try:
                page_title = dom_tree.xpath('//title')[0].text_content()
            except IndexError:
                page_title = 'Not Found'

            try:
                page_h1 = dom_tree.xpath('//h1')[0].text_content()
            except IndexError:
                page_h1 = 'Not Found'

            page = {"url": url, "title": page_title.strip(), "h1": page_h1.strip()}

            await objects.create(Page, **page)

            print('OK', page)

            with open('results.csv', 'a') as f:
                f.write(f'{url}\t{page_title}\t{page_h1}\n')

            for link_data in dom_tree.iterlinks():

                link = link_data[2]
                link = link.split('#')[0]

                if domain not in link:
                    continue

                if any(part in link for part in BAD_PARTS):
                    continue

                if link in SCANNED_LINKS:
                    continue

                if link in LINKS_QUEUE:
                    continue

                LINKS_QUEUE.add(link)


async def main():
    domain = input('Enter domain: ')
    home_page = f'https://{domain}/'
    LINKS_QUEUE.add(home_page)

    thread = 200
    tasks = []
    for _ in range(thread):
        tasks.append(worker(domain))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
 