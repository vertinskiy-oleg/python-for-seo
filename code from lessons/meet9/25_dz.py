import asyncio
import aiohttp
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from requests_html import AsyncHTMLSession


loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=4)


async def coro1():
    while True:
        await asyncio.sleep(0.1)
        print("Coro 1 Working!")


async def coro2():
    while True:
        await asyncio.sleep(0.2)
        print("Coro 22222222 Working!")


def coro3():
    sleep(0.2)
    print("Coro 3333333 Working!")


async def acoro3():
    while True:
        await loop.run_in_executor(executor, coro3)

# async def coro3():
#     session = AsyncHTMLSession()
#     while True:
#         response = session.get('https://py4you.com/')
#         await asyncio.sleep(0.3)
#         await response
#         print(f'[{response.result()}] https://py4you.com/')


async def main():
    task1 = coro1()
    task2 = coro2()
    task3 = acoro3()
    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    loop.run_until_complete(main())
