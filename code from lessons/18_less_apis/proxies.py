import os
import random
import pickle
from pprint import pprint
from requests_html import HTMLSession
from datetime import datetime


def get_random_proxy():

    now_time = datetime.now()

    if 'proxies.pickle' in os.listdir('.'):
        with open('proxies.pickle', 'rb') as f:
            proxies_dump = pickle.load(f)
            dump_time = proxies_dump[0]
            proxy_list = proxies_dump[1]
    else:
        dump_time = None

    if not dump_time or (now_time - dump_time).seconds > 10:

        api_url = 'http://api.best-proxies.ru/proxylist.json'

        query_params = {
            'key': 'b19654c5120f874a607ce27cf1c229f4',
            'type': 'socks4',
            'google': 1,
            'limit': 0
        }

        with HTMLSession() as session:
            response = session.get(api_url, params=query_params)

        dump_time = datetime.now()
        proxy_list = response.json()

        with open('proxies.pickle', 'wb') as f:

            pickle.dump((dump_time, proxy_list), f)

    random_proxy = random.choice(proxy_list)

    proxies = {
        'http': f"socks4://{random_proxy['ip']}:{random_proxy['port']}",
        'https': f"socks4://{random_proxy['ip']}:{random_proxy['port']}"
    }

    return proxies


if __name__ == '__main__':
    random_pr = get_random_proxy()
    pprint(random_pr)
