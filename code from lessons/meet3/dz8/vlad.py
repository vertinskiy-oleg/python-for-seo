from requests_html import HTMLSession


def input_data():
    url = input('Enter URL: ')
    keyword = input('Enter Keyword: ')
    return url, keyword


def my_parser(url):
    with HTMLSession() as session:
        resp = session.get(url)

    try:
        title = resp.html.xpath('//title')[0].text
    except Exception as e:
        print('Title not found on the page', e)
        title = ''

    try:
        description = resp.html.xpath('//meta[@name="description"]/@content')[0]
    except Exception as e:
        print('Description not found on the page', e)
        description = ''

    try:
        h1 = resp.html.xpath('//h1')[0].text
    except Exception as e:
        print('H1 not found on the page', e)
        h1 = ''
    return title, description, h1


def my_count(title, description, h1, keyword):
    title_words_count = len([x for x in title.split() if len(x) > 2])
    description_words_count = len([x for x in description.split() if len(x) > 2])
    h1_words_count = len([x for x in title.split() if len(x) > 2])

    p_keywords_in_title = round((title.lower().count(keyword) /
                                 title_words_count) * 100)
    p_keywords_in_description = round((description.lower().count(keyword) /
                                       description_words_count) * 100)
    p_keywords_in_h1 = round((h1.lower().count(keyword) /
                              h1_words_count) * 100)

    return p_keywords_in_title, p_keywords_in_description, p_keywords_in_h1


def seo_count(p_keywords_in_title, p_keywords_in_description,
              p_keywords_in_h1):

    if 2 <= p_keywords_in_description < 10:
        description_quality = {x: (x - 2) * 2
                               for x in range(2, 17)}[p_keywords_in_description]
    else:
        description_quality = 0

    if 1 < p_keywords_in_title < 10:
        title_quality = 20
    elif 10 <= p_keywords_in_title <= 20:
        title_quality = 40
    else:
        title_quality = 0

    h1_quality = 30 if p_keywords_in_h1 > 0 else 0

    page_quality = title_quality + description_quality + h1_quality

    return page_quality


def main():
    url, keyword = input_data()
    title, descr, h1 = my_parser(url)
    keywords_data = my_count(title, descr, h1, keyword)
    page_quality = seo_count(*keywords_data)
    print(f'\nSEO Page {url} Quality is: {page_quality}\n')


if __name__ == '__main__':
    main()
