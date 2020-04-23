from requests_html import HTMLSession
from random import sample

session = HTMLSession()


def parse_google(key):
    engine_link = f'https://www.google.com/search?q={key}&num=10&hl=en'
    resp = session.get(engine_link)
    html_snippets = resp.html.xpath('//div[@class="g"]')

    top = []

    for html_item in html_snippets:
        href = html_item.xpath('//div[@class="r"]/a[1]/@href')[0]
        top.append(href)

    top3 = sample(top, 3)

    texts = []

    for site in top3:
        resp = session.get(site)
        try:
            texts.append(resp.html.find('p')[0].text)
        except Exception as e:
            print(e, type(e))

    return texts


if __name__ == 'main':
    parse_google('python')
