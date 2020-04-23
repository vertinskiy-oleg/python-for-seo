from qwerty import HTMLSession


SETTING = 'num=100'


def get_domain(url):
    dom = url.split('/')[2]
    if dom.startswith('www.'):
        dom = dom[4:]
    return dom


def google_scraper(keyword, lang='en', serp_count=10):
    session = HTMLSession()

    resp = session.get(
        f'https://www.google.com/search?q={keyword}&'
        f'num={serp_count}&hl={lang}')

    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')

    # if len(links) > 5:
    #     return links

    domains = [get_domain(link) for link in links
               if link.startswith('http')]

    similar_elements = resp.html.xpath(
        '//div[@class="card-section"]//p')

    similar_keys = [el.text.strip()
                    for el in similar_elements]

    return domains, similar_keys


if __name__ == '__main__':
    result = google_scraper('test')
    print(result)
    print('1111111111111111111111111111111111111')
    print('2222222222222222222222222222222222222')
    print('3333333333333333333333333333333333333')
