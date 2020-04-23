"""

python3 dz26_bing_parser.py

[]Задача 1:
В асинхронном парсере написанном на занятии был реализован аналог Screaming Frog SEO Spider.
Переделать его таким образом, чтобы он стал парсером выдачи поисковой системы bing.com.
Ключи для сбора сайтов из SERP считываем из файла. Результат сохраняем в базу.
Оценка за задачу - 200 баллов.

"""

import asyncio
import aiohttp
import random
from lxml import html
# from dz26_db import Page, objects
from time import sleep

with open('ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]

with open('keys.txt', 'r', encoding='utf-8') as f:
    KEYS_QUEUE = {line.strip() for line in f}

SCANNED_KEYS = set()


async def get_serp():
    async with aiohttp.ClientSession() as session:
        while True:

            if len(KEYS_QUEUE) == 0:
                await asyncio.sleep(3)
                if len(KEYS_QUEUE) == 0:
                    break
                continue

            key = KEYS_QUEUE.pop()
            SCANNED_KEYS.add(key)

            print('SEND', key)
            try:
                rand_headers = {'User-Agent': random.choice(USER_AGENTS)}
                engine_link = f'https://www.bing.com/search?q={key}&count=50'
                resp = await session.get(engine_link, headers=rand_headers)
                html_code = await resp.text()
                dom_tree = html.fromstring(html_code)
                # breakpoint()
                try:
                    html_snipets = dom_tree.xpath('//li[@class="b_algo"]')
                except Exception as e:
                    print(f'Ошибка парсинга сниппетов', e, type(e))
                    continue
                if len(html_snipets) == 0:
                    print(f'Ошибка парсинга сниппетов: вернуло 0 результатов')

                # debug:
                # print(rand_headers)
                # with open('duck.html', 'w') as output_file:
                #     output_file.write(resp.text)

                link = title = description = 'not-found'

                for snipet in html_snipets:

                    try:
                        link = snipet.xpath('.//h2/a/@href')
                    except Exception as e:
                        print(f'Ошибка xpath ссылки из сниппета', e, type(e))

                    try:
                        title = snipet.xpath('.//h2')[0].text_content()
                    except Exception as e:
                        print(f'Ошибка xpath title из сниппета', e, type(e))

                    try:
                        description = snipet.xpath('.//div[@class="b_caption"]/p')[0].text_content()
                    except Exception as e:
                        print(f'Ошибка xpath description из сниппета', e, type(e))

                    page = {"url": link, "title": title.strip(), "description": description.strip()}

                    # await objects.create(Page, **page)

                    print('OK', page)

                    key_result = f'{key}\t{link}\t{title}\t{description}\n'

                    with open('results.csv', 'a') as f3:
                        f3.write(key_result)

            except Exception as e:
                print(f'Ошибка парсинга выдачи', e, type(e))
                continue

            request_random_timeout = random.randint(5, 15)
            print(f'[OK] {key} | sleep: {request_random_timeout} sec')
            # await asyncio.sleep(request_random_timeout)


async def main():
    thread = 2
    tasks = []
    for _ in range(thread):
        tasks.append(get_serp())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())