# a = range(10)
# for i in a:
#     print(i)


# domains = ['asdads.com', 'qweqweqwe.com', 'reyrtyrty.com']
# my_gen = (x for x in domains)
# for i in my_gen:
#     print(i)


def ip_gen():
    for ip1 in range(256):
        for ip2 in range(256):
            for ip3 in range(256):
                for ip4 in range(256):
                    ip = f'{ip1}.{ip2}.{ip3}.{ip4}'
                    yield ip


res = ip_gen()

ip = res.__next__()
ip = res.__next__()
ip = res.__next__()
ip = res.__next__()
ip = res.__next__()

print(ip)


# for ip in res:
#     print(ip)
