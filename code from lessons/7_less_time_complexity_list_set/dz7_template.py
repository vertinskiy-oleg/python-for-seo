import random
from time import sleep
from pprint import pprint
from requests_html import HTMLSession


keywords = (
    'buy essays online',
    'buy essay',
    'write my essay',
    'write history essay'
)

session = HTMLSession()


SERP = {}


for key in keywords:
    print(f'Send request to Google: [{key}]')
    resp = session.get(f'https://www.google.com/search?q={key}&num=100&hl=en')
    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
    SERP[key] = [x.split('/')[2] for x in links if 'http' in x]
    sleep_seconds = random.randint(1, 10)
    print(f'Sleep: {sleep_seconds}')
    sleep(sleep_seconds)


pprint(SERP)

# Ваш код писать тут...

