from concurrent.futures import ThreadPoolExecutor


def worker1():
    for i in range(100):
        print('Thread1 working')


def worker2():
    for i in range(100):
        print('222222222222')


def worker3():
    for i in range(100):
        print('33333333333333')


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(worker1)
    executor.submit(worker2)
    executor.submit(worker3)


for i in range(100):
    print('main thread!')
