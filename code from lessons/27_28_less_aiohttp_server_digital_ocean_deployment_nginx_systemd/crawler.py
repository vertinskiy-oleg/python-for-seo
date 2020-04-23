import asyncio
import aiohttp
from time import time
from lxml import html
from model import Page, objects


BAD_PARTS = {
    '.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi', '.css',
    '.mp4', '.webm', '.ico', '/static/', '/media/', '/summernote/'
}

GOOGLE_BOT = '''Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) 
AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 
(compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)'''.replace('\n', '')


LINKS_QUEUE = set()
SCANNED_LINKS = set()


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
                print('SEND', url)

                google_headers = {'User-Agent': GOOGLE_BOT}

                t1 = time()
                resp = await session.get(url, headers=google_headers)
                t2 = time()

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
                page_description = dom_tree.xpath('//meta[@name="description"]/@content')[0]
            except IndexError:
                page_title = 'Not Found'

            try:
                page_h1 = dom_tree.xpath('//h1')[0].text_content()
            except IndexError:
                page_h1 = 'Not Found'

            page = {
                "url": url,
                "response_time": round(t2-t1, 2),
                "title": page_title.strip(),
                "title_len": len(page_title.strip()),
                "h1": page_h1.strip(),
                "description": page_description,
                "description_len": len(page_description),
                "domain": domain
            }

            await objects.create(Page, **page)

            print('OK', page)

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


async def start_crawl(domain):
    home_page = f'https://{domain}/'
    LINKS_QUEUE.add(home_page)

    thread = 10
    tasks = []
    for _ in range(thread):
        tasks.append(worker(domain))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(start_crawl('py4you.com'))
