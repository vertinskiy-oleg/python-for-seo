from time import time
from requests_html import HTMLSession


def time_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print('Время выполнения', t2 - t1)
        with open('log.txt', 'a') as f:
            f.write(f'{func.__name__} | время выполнения - {t2-t1} секунд\n')
        return result
    return wrapper


def get_domain(url):
    dom = url.split('/')[2]
    if dom.startswith('www.'):
        dom = dom[4:]
    return dom


@time_decorator
def get_schema(url):
    result = url.split('/')[0][:-1]
    return result


@time_decorator
def google_scraper(keyword, lang='en', serp_count=10):
    session = HTMLSession()
    resp = session.get(
        f'https://www.google.com/search?q={keyword}&'
        f'num={serp_count}&hl={lang}')
    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
    domains = [get_domain(link) for link in links
               if link.startswith('http')]
    similar_elements = resp.html.xpath(
        '//div[@class="card-section"]//p')
    similar_keys = [el.text.strip()
                    for el in similar_elements]
    return domains, similar_keys


@time_decorator
def factorial1(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@time_decorator
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


# r1 = factorial1(100000)
# r2 = factorial1(100000)


# url = 'https://py4you.com/courses/python-for-seo/'
#
# domain = get_domain(url)
# schema = get_schema(url)
#
results = google_scraper('buy iphone X')


# print(results)
# print(domain)


names = []

for dom in results[0]:
    zone = dom.split('.')[0]
    names.append(zone)


def qwe(dom):
    return dom.split('.')[0]


names2 = list(map(qwe, results[0]))

print(names)
print(names2)
