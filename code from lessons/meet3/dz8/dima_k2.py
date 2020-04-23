from requests_html import HTMLSession
import sys

url = input('Enter URL: ')
keyword = input('Enter Keyword: ')

# Stopping Code Execution when user types in "exit"
if input() == "exit":
    sys.exit()

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

print('*' * 50)
print('TITLE:', title)
print('*' * 50)
print('DESCRIPTION:', description)
print('*' * 50)
print('H1:', h1)
print('*' * 50)

# Ваш код домашнего задания писать тут...

# improving SEO score depending on keyword frequency in url, title, description and h1


def url_keyword_analyzer(url):
    seo_score_url = 0
    keyword_amount_in_url = url.lower().count(keyword)
    if keyword_amount_in_url == 1:
        seo_score_url += 15
    return seo_score_url


# too many keywords (3 and more) in title will decrease the SEO score
def title_keyword_analyzer(your_title):
    seo_score_1 = 0
    keyword_amount_in_title = your_title.lower().count(keyword)
    if keyword_amount_in_title == 1:
        seo_score_1 += 25
    elif keyword_amount_in_title > 2:
        seo_score_1 -= 10
    return seo_score_1


# too many keywords (4 and more) in description will decrease the SEO score
def description_keyword_analyzer(your_description):
    seo_score_2 = 0
    keyword_amount_in_description = your_description.lower().count(keyword)
    if keyword_amount_in_description in range(1, 4):
        seo_score_2 += 10
    else:
        seo_score_2 -= 5
    return seo_score_2


# too many keywords (2 and more) in h1 will decrease the SEO score
def h1_keyword_analyzer(your_h1):
    seo_score_3 = 0
    keyword_amount_in_h1 = your_h1.lower().count(keyword)
    if keyword_amount_in_h1 == 1:
        seo_score_3 += 20
    elif keyword_amount_in_h1 > 1:
        seo_score_3 -= 10
    return seo_score_3


# influence of the keyword position in title on SEO score

def title_keyword_position_analyzer(your_title):
    seo_score_4 = 0
    title_list = your_title.lower().split()
    try:
        keyword_index_title = int(title_list.index(keyword))

        if keyword_index_title == 0:
            seo_score_4 += 15
        elif keyword_index_title == 1:
            seo_score_4 += 10
        elif keyword_index_title == 2:
            seo_score_4 += 5
    except:
        pass
    return seo_score_4


# influence of the keyword position in description on SEO score

def description_keyword_position_analyzer(your_description):
    seo_score_5 = 0
    description_list = your_description.lower().split()
    try:
        keyword_index_description = int(description_list.index(keyword))

        if keyword_index_description == 0:
            seo_score_5 += 5
    except:
        pass
    return seo_score_5


# influence of the keyword position in h1 on SEO score

def h1_keyword_position_analyzer(your_h1):
    seo_score_6 = 0
    h1_list = your_h1.lower().split()
    try:
        keyword_index_h1 = int(h1_list.index(keyword))
        if keyword_index_h1 == 0:
            seo_score_6 += 10
    except:
        pass
    return seo_score_6


my_analyzer = url_keyword_analyzer


analyzers = [
    url_keyword_analyzer, title_keyword_analyzer, description_keyword_analyzer,
    h1_keyword_analyzer, title_keyword_position_analyzer,
    description_keyword_position_analyzer, h1_keyword_position_analyzer
]


seo_score = 0


for analyzer in analyzers:
    if 'url_' in analyzer.__name__:
        data = url
    elif 'title_' in analyzer.__name__:
        data = title
    elif 'h1_' in analyzer.__name__:
        data = h1
    elif 'description_' in analyzer.__name__:
        data = description
    else:
        raise ValueError('Unknown analyzer type')

    seo_score += analyzer(data)


# seo_score = my_analyzer(url)
# seo_score += title_keyword_analyzer(title)
# seo_score += description_keyword_analyzer(description)
# seo_score += h1_keyword_analyzer(h1)
# seo_score += title_keyword_position_analyzer(title)
# seo_score += description_keyword_position_analyzer(description)
# seo_score += h1_keyword_position_analyzer(h1)

print(f'SEO Page Quality equals to: {seo_score}')
