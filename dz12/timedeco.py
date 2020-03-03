from time import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print('Completion time', t2 - t1)
        with open('log.txt', 'a') as f:
            f.write(f'{func.__name__} completion - {t2 - t1} sec\n')
        return result

    return wrapper
