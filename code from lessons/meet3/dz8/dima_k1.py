from requests_html import HTMLSession


def word_count(on_page_words):
    on_page_words.split()
    var2 = len(on_page_words)
    return var2


def title_density_mark_calc(elem_kw_perc):
    if 1 <= elem_kw_perc <= 20:
        mark_kw_title_perc = 15
    elif 20 < elem_kw_perc <= 30:
        mark_kw_title_perc = 10
    else:
        mark_kw_title_perc = 0

    return mark_kw_title_perc


def density_mark_calc(elem1_kw_perc, elem2_kw_perc):
    if (elem1_kw_perc >= 5) and (elem2_kw_perc <= 10):
        mark_kw_perc = 15
    elif (elem1_kw_perc > 10) and (elem1_kw_perc <= 15):
        mark_kw_perc = 10
    else:
        mark_kw_perc = 0

    return mark_kw_perc


def kw_pos_mark_func(list_name):
    j = 0
    for i in list_name:
        if list_name[j] != keyword:
            j += 1
    else:
        kw_pos_in_elem = j
        if kw_pos_in_elem <= 4:
            kw_position_title_mark = 5
        else:
            kw_position_title_mark = 0

    return kw_position_title_mark


def kw_in_mark_func(elem_kw_density, mind=1, maxd=3):
    if mind < elem_kw_density < maxd:
        kw_in_mark = 15
    else:
        kw_in_mark = 0
    return kw_in_mark


def kw_in_h1_mark_func(elem_kw_density):
    if elem_kw_density < 1:
        kw_in_h1_mark = 0
    elif elem_kw_density > 5:
        kw_in_h1_mark = 0
    else:
        kw_in_h1_mark = 15

    return kw_in_h1_mark


def page_crawler(url):
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

    return title, h1, description


def main(title, description, h1):
    title_kw_density = title.lower().count(keyword)
    description_kw_density = description.lower().count(keyword)
    h1_kw_density = h1.lower().count(keyword)

    title_words = word_count(title)
    description_words = word_count(description)
    h1_words = word_count(h1)

    # round(100 * keyword_density / word_counter)
    title_kw_perc = round(100 * title_kw_density / title_words)

    try:
        description_kw_perc = round(100 * description_kw_density / description_words)
    except ZeroDivisionError:
        description_kw_perc = 0
        print('Description fot found')

    h1_kw_perc = round(100 * h1_kw_density / h1_words)

    mark_kw_title_perc = title_density_mark_calc(title_kw_perc)
    mark_kw_descr_perc = density_mark_calc(description_kw_perc, title_kw_perc)
    mark_kw_h1_perc = density_mark_calc(h1_kw_perc, title_kw_perc)

    kw_density_mark = mark_kw_title_perc + mark_kw_descr_perc + mark_kw_h1_perc
    # <--kw density mark ends

    # kw position in text mark starts-->
    list_title = title.split()
    list_description = description.split()

    kw_position_title_mark = kw_pos_mark_func(list_title)
    kw_position_description_mark = kw_pos_mark_func(list_description)

    kw_position_mark = kw_position_title_mark + kw_position_description_mark
    # <--kw position in text mark ends

    # kw in text mark starts-->

    kw_in_title_mark = kw_in_mark_func(title_kw_density)
    kw_in_description_mark = kw_in_mark_func(title_kw_density, 2, 4)
    kw_in_h1_mark = kw_in_h1_mark_func(h1_kw_density)

    kw_in_text_mark = kw_in_title_mark + kw_in_description_mark + kw_in_h1_mark
    # <--kw in text mark ends

    # final mark count
    mark = kw_density_mark + kw_position_mark + kw_in_text_mark

    print('\nSEO Page Quality is:', mark)


if __name__ == '__main__':
    while True:
        url = input('Enter URL (or "exit" if you want to quit): ')

        if url == 'exit':
            quit()

        keyword = input('Enter Keyword: ').lower()

        title, h1, description = page_crawler(url)

        print('*'*50)
        print('TITLE:', title)
        print('*'*50)
        print('DESCRIPTION:', description)
        print('*'*50)
        print('H1:', h1)
        print('*'*50)

        main(title, description, h1)
