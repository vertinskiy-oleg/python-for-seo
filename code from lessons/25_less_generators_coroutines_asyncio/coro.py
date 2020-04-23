import asyncio


async def coro1():
    while True:
        await asyncio.sleep(0.02)
        print("Coro 1 Working!")


async def coro2():
    while True:
        await asyncio.sleep(0.01)
        print("Coro 22222222 Working!")


async def main():
    task1 = coro1()
    task2 = coro2()
    await asyncio.gather(task1, task2)


asyncio.run(main())
