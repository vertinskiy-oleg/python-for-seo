from time import time
from requests_html import HTMLSession
from reppy.robots import Robots
from content_watch import get_uniquness_of_url
from proxies import get_random_proxy


session = HTMLSession()


domain = input('Введите домен для краулинга: ')
first_link = f'http://{domain}/'

prepared_response = session.get(first_link, proxies={})
first_link = prepared_response.url
domain = first_link.split('/')[2]

robots_link = f'https://{domain}/robots.txt'

crawled_links = set()

links_to_crawl = set()
links_to_crawl.add(first_link)

robots = Robots.fetch(robots_link)

file_results = open('checking_results.txt', 'w', encoding='utf-8')


while True:

    if len(links_to_crawl) == 0:
        break
    url = links_to_crawl.pop()

    try:
        proxies = get_random_proxy()

        t1 = time()
        response = session.get(url, proxies=proxies, timeout=8)
        t2 = time()

        crawled_links.add(url)
        bad_parts = ['cdn-cgi', '.jpg', '.gif']

        for link in response.html.absolute_links:
            if domain not in link:
                continue
            if not robots.allowed(link, '*'):
                continue
            if any(x in link for x in bad_parts):
                continue
            if link in crawled_links:
                continue
            links_to_crawl.add(link)

        # uniq = get_uniquness_of_url(url, domain)

        result = f'[response_time: {round(t2-t1, 2)} sec]\t[proxy: {proxies["http"]}]\t{url}'
        print(result)

        file_results.write(result+'\n')
        file_results.flush()

    except KeyboardInterrupt:
        breakpoint()

    except Exception as e:
        print(e, type(e))
        links_to_crawl.add(url)
