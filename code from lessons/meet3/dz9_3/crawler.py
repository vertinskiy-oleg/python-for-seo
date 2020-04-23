from time import time
from requests_html import HTMLSession
from reppy.robots import Robots


session = HTMLSession()


domain = input('Введите домен для краулинга: ')
first_link = f'http://{domain}/'

prepared_response = session.get(first_link)
first_link = prepared_response.url
domain = first_link.split('/')[2]

robots_link = f'https://{domain}/robots.txt'

crawled_links = set()

links_to_crawl = set()
links_to_crawl.add(first_link)

robots = Robots.fetch(robots_link)


def scan_url(url):
    t1 = time()
    response = session.get(url)
    t2 = time()
    crawled_links.add(url)
    bad_parts = ['cdn-cgi', '.jpg', '.gif']
    filtered_links = set()
    for link in response.html.absolute_links:
        if domain not in link:
            continue
        if not robots.allowed(link, '*'):
            continue
        if any(x in link for x in bad_parts):
            continue
        if link in crawled_links:
            continue
        filtered_links.add(link)
    return filtered_links, round(t2-t1, 2)


while True:
    if len(links_to_crawl) == 0:
        break
    url = links_to_crawl.pop()
    new_links, page_time = scan_url(url)
    links_to_crawl = links_to_crawl.union(new_links)

    print(f'[{page_time} sec] [OK] {url}')
