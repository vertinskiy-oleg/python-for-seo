from requests_html import HTMLSession
from reppy.robots import Robots
from pprint import pprint

start_url = 'http://quotes.toscrape.com/'
visited = set()

session = HTMLSession()

def get_links(url):
    r = session.get(url)
    page_links = {
        l for l in r.html.absolute_links if start_url in l}
    return page_links

def crawl(url):
    for l in get_links(url):
        if l in visited:
            continue
        visited.add(l)
        crawl(l)

def check_allow(urls):
    robots = Robots.fetch(f'{start_url}/robots.txt')
    return {url for url in urls if robots.allowed(url, 'Googlebot') == True}

crawl(start_url)

with open('allowed_links.txt', 'w') as f:
    f.writelines(l + '\n' for l in check_allow(visited))