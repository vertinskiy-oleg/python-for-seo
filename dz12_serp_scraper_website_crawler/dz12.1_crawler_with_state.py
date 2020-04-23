import pickle
import os
from time import time
from requests_html import HTMLSession
from reppy.robots import Robots

domain = ''
crawled_links = set()
links_to_crawl = set()
file_results = None


def make_request(url):
    session = HTMLSession()
    return session.get(url)


def parse_robots(domain):
    robots_link = f'https://{domain}/robots.txt'
    return Robots.fetch(robots_link)


def init_crawl():
    global domain, file_results
    domain = input('Введите домен для краулинга: ')
    first_link = f'https://{domain}/'

    prepared_response = make_request(first_link)
    first_link = prepared_response.url

    links_to_crawl.add(first_link)

    file_results = open('checking_results.txt', 'w', encoding='utf-8')


if os.path.exists('last_saved_crawl.pickle'):
    continue_last_crawl = input('Do you want to continue last crawl? (y/n): ')
    if continue_last_crawl == 'y':
        with open('last_saved_crawl.pickle', 'rb') as f:
            crawled_links, links_to_crawl, domain = pickle.load(f)
            file_results = open('checking_results.txt', 'a', encoding='utf-8')
    else:
        init_crawl()
else:
    init_crawl()

while True:

    try:

        if len(links_to_crawl) == 0:
            break
        url = links_to_crawl.pop()

        t1 = time()
        response = make_request(url)
        t2 = time()

        crawled_links.add(url)
        bad_parts = ['cdn-cgi', '.jpg', '.gif']

        for link in response.html.absolute_links:
            if domain not in link:
                continue
            if not parse_robots(domain).allowed(link, '*'):
                continue
            if any(x in link for x in bad_parts):
                continue
            if link in crawled_links:
                continue
            links_to_crawl.add(link)

        result = f'[{round(t2 - t1, 2)} sec] [OK] {url}'
        print(result)

        file_results.write(result + '\n')
        file_results.flush()

    except KeyboardInterrupt:
        with open('last_saved_crawl.pickle', 'wb') as f:
            pickle.dump((crawled_links, links_to_crawl, domain), f)
        exit()

if os.path.exists('last_saved_crawl.pickle'):
    os.remove('last_saved_crawl.pickle')




