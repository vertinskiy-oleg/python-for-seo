from requests_html import HTMLSession
from pprint import pprint

session = HTMLSession()

r = session.get('https://habr.com/')

internal_page_links = []

for link in r.html.absolute_links:
    if '//habr.com' in link:
        internal_page_links.append(link)

pprint(internal_page_links)
