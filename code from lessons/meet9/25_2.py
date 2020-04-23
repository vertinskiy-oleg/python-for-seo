"""
python3 dz25.py

В папке лежит скрипт coro.py в этом скрипте добавить 3-ю корутину.
Делающую асинхронный запрос на главную страницу py4you.com.
Оценка за задачу - 80 баллов.
"""
import uvloop
import asyncio
from requests_html import AsyncHTMLSession


async def coro1():
    while True:
        await asyncio.sleep(0.03)
        print("Coro 1 Working!")


async def coro2():
    while True:
        await asyncio.sleep(0.02)
        print("Coro 22222222 Working!")


async def coro3():
    while True:
        await asyncio.sleep(0.01)
        url = 'https://py4you.com/'
        with AsyncHTMLSession() as session:
            resp = await session.get(url)
            title = resp.html.xpath('//title')[0].text
            h1 = resp.html.xpath('//h1')[0].text
            print(f'Тайтл страницы: {title}\nЗаголовок h1 страницы: {h1}')


async def main():
    task1 = coro1()
    task2 = coro2()
    task3 = coro3()
    await asyncio.gather(task1, task2, task3)


uvloop.install()
asyncio.run(main())
