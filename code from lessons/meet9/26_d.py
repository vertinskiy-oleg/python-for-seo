import asyncio
import aiohttp
import random
from lxml import html
# from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector


# with open('proxies.txt', 'r') as f:
#     PROXIES = [line.strip() for line in f if line.strip()]

with open('ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]

with open('keys.txt', 'r') as f:
    KEYWORDS = [line.strip() for line in f if line.strip()]


async def bing_scraper():
    for keyword in KEYWORDS:
        try:
            print('SEND', keyword)

            rand_headers = {'User-Agent': random.choice(USER_AGENTS)}
            # random_ip = random.choice(PROXIES)
            # connector = ProxyConnector.from_url(f'socks5://{random_ip}')

            async with aiohttp.ClientSession() as session:
                resp = await session.get(f'https://www.bing.com/search?q={keyword}', headers=rand_headers)
                html_code = await resp.text()

            assert resp.status == 200

        except Exception as e:
            print(e, type(e))
            continue

        try:
            dom_tree = html.fromstring(html_code)
        except ValueError:
            continue

        snipets = dom_tree.xpath('///*[@id="b_results"]/li[3]')

        search_results = []

        for sn in snipets:

            title = sn.xpath('//h2')[0].text_content()
            description = sn.xpath('///*[@id="b_results"]/li[2]/div/div[1]/p')[0].text_content()
            url = sn.xpath('//*[@id="b_results"]/li[2]/div/div[1]/div')[0].text_content()

            data = {
                        'title': title,
                        'description': description,
                        'url': url
                    }

            search_results.append(data)

            with open('results.csv', 'a') as f:
                f.write(f'{url}\t{title}\t{description}\n')


async def main():

    thread = 2
    tasks = []
    for _ in range(thread):
        tasks.append(bing_scraper())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
