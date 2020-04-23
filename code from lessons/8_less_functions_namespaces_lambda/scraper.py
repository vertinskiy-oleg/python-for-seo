from pprint import pprint
from qwerty import HTMLSession


my_keys = [
    'buy laptop',
    'buy xiaomi',
    'buy iphone',
    # 'buy samsung'
]


def google_craper(keyword, lang='en', serp_count=10):

    session = HTMLSession()
    resp = session.get(
        f'https://www.google.com/search?q={keyword}&num={serp_count}&hl={lang}')
    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')

    if len(links) > 5:
        return links

    domains = [x.split('/')[2] for x in links if 'http' in x]
    similar_elements = resp.html.xpath('//div[@class="card-section"]//p')
    similar_keys = [el.text.strip() for el in similar_elements]

    return domains, similar_keys


# result = {}
#
# for key in my_keys:
#     input_data1 = [key, 10, 'en']
#     input_data2 = {
#         'keyword': key,
#         'lang': 'en'
#     }
#     data = google_craper(key)
#     result[key] = data
#
# pprint(result)

# ====================================================

# result2 = lambda key: ' '.join(key.split()[:2])
#
#
# def result3(key):
#     result = ' '.join(key.split()[:2])
#     return result
#
#
# print(result2('asdad asd ad a sad'))
#
# print(google_craper)
# print(result2)


domains = [
    'xiaomi-buy.com.ua',
    'www.xiaomi.ua',
    'www.xiaomi.ua',
    'stylus.ua',
    'rozetka.com.ua',
    'mi-shop.com',
    'www.mi.com',
    'www.mi.com',
    'www.moyo.ua',
    'www.citrus.ua',
    'mi.by',
    'www.citrus.ua',
    'www.vodafone.ua',
    'allo.ua',
    'allo.ua',
    'ru-mi.com',
    'mi-shop.by',
    'www.gearbest.com',
    'www.a1.by',
    'pn.com.ua',
    'hotline.ua',
    'www.honorbuy.com',
    'touch.com.ua',
    'mishka-shop.com',
    'market.yandex.ru',
    'www.dns-shop.ru',
    'www.kimovil.com',
    'catalog.onliner.by'
]


def sort_func(x):
    return x[4:] if x.startswith('www') else x


domains.sort(key=sort_func)

print(domains)


breakpoint()
