from requests_html import HTMLSession
from pprint import pprint

session = HTMLSession()
r = session.get('https://habr.com/')

internal_links = sorted(
    {l for l in r.html.absolute_links if 'https://habr.com' in l})
pprint(internal_links)
