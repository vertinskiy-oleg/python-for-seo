import re
from requests_html import HTMLSession


def parse_meta(url):
    """Parse title, description, h1"""
    with HTMLSession() as session:
        resp = session.get(url)
    try:
        title = resp.html.xpath('//title')[0].text
    except Exception as e:
        print('Title not found on the page', e)
        title = ''

    try:
        description = resp.html.xpath(
            '//meta[@name="description"]/@content')[0]
    except Exception as e:
        print('Description not found on the page', e)
        description = ''

    try:
        h1 = resp.html.xpath('//h1')[0].text
    except Exception as e:
        print('H1 not found on the page', e)
        h1 = ''

    return title, description, h1


def get_stats(s, key):
    """Get stats from title, description, h1"""
    regex = r"(:|\/|\.|-|\||')"
    s_cleared = (re.sub(regex, ' ', s)).lower()
    l = s_cleared.split()
    l_cleared = [s for s in l if s != '']

    if s:
        symbols_count = len(s_cleared)
        words_count = len(l_cleared)
        keyword_count = s_cleared.count(key)
        keyword_density = round(keyword_count / words_count * 100)
        keyword_position = s_cleared.find(key)
    else:
        symbols_count = words_count = keyword_count = keyword_density = keyword_position = 0

    return {'symbols': symbols_count,
            'words': words_count,
            'key_count': keyword_count,
            'key_density': keyword_density,
            'key_pos': keyword_position}


def analyze_seo_score(url, keyword):
    """Analyse SEO Score"""
    title, desc, h1 = parse_meta(url)
    title_stats = get_stats(title, keyword)
    description_stats = get_stats(desc, keyword)
    h1_stats = get_stats(h1, keyword)

    seo_score = 0

    # Title Check (Max - 50)
    if title_stats['key_count']:
        seo_score += 15
        if title_stats['key_density'] > 5:
            seo_score += 20
        elif title_stats['key_density'] > 3:
            seo_score += 15
        else:
            seo_score += 5
        if title_stats['key_pos'] < title_stats['symbols'] / 3:
            seo_score += 15
    # Description Check (Max - 30)
    if description_stats['key_count']:
        seo_score += 10
        if description_stats['key_density'] > 5:
            seo_score += 10
        elif description_stats['key_density'] > 3:
            seo_score += 5
        else:
            seo_score += 1
        if description_stats['key_pos'] < description_stats['symbols'] / 3:
            seo_score += 10
    # H1 Check (Max - 20)
    if h1_stats['key_count']:
        seo_score += 10
        if h1_stats['key_density'] > 5:
            seo_score += 5
        elif h1_stats['key_density'] > 3:
            seo_score += 2
        else:
            seo_score += 1
        if h1_stats['key_pos'] < h1_stats['symbols'] / 3:
            seo_score += 5

    return seo_score
