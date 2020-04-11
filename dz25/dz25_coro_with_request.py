import asyncio
import aiohttp


async def coro1():
    while True:
        await asyncio.sleep(0.02)
        print("Coro 1 Working!")

async def coro2():
    while True:
        await asyncio.sleep(0.01)
        print("Coro 22222222 Working!")

async def coro3():
    while True:
        async with aiohttp.ClientSession() as session:
            res = await session.get('https://py4you.com')
            print(f'py4you.com status: {res.status}')
                


async def main():
    task1 = coro1()
    task2 = coro2()
    task3 = coro3()
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
