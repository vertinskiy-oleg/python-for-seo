from scraper import SETTING as SCRAPER_SETTING
from scraper import get_domain, google_scraper


my_keys = [
    'buy laptop',
    'buy xiaomi',
    'buy iphone'
]


print(SCRAPER_SETTING)


SETTING = 111111


print(SETTING)


url = 'https://py4you.com/courses/python-for-seo/'

print(locals())
print('*'*50)
print(globals())

my_dom = get_domain(url)

print(my_dom)

result = {}

for key in my_keys:
    result[key] = google_scraper(key)

print(result)
