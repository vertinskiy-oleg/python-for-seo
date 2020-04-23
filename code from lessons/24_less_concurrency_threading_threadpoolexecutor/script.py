from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor


links = [1, 2, 3]


locker = Lock()


def worker1():
    # with locker:
    for i in range(100):
        links.append(1)
        print('Thread1 working')
        # links.remove(2)


thread1 = Thread(target=worker1)
thread1.start()


def worker2():
    # with locker:
    for i in range(100):
        links.append(2)
        print('222222222222')
        # links.remove(3)


thread2 = Thread(target=worker2)
thread2.start()


def worker3():
    # with locker:
    for i in range(100):
        links.append(3)
        print('33333333333333')
        # links.remove(1)


thread2 = Thread(target=worker3)
thread2.start()
