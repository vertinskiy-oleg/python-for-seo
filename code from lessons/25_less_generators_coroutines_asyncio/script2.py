def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)


c = calc()

# Необходимая инициация. Можно написать c.send(None)
c.__next__()

# Выведет 3
c.send((1, 2))

# Выведет 130
c.send((100, 30))

# Выведет 666
c.send((666, 0))

# Выведет [3, 130, 666]
c.send(('h', 0))

# Закрывем генератор
c.close()
