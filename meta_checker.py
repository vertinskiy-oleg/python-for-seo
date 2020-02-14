import re
from pprint import pprint

url = 'https://qarea.com/services/custom-software-development'
title = 'Custom Software Development Services | QArea'
description = '''Custom Software Development Services by QArea, 
  an outsourcing software development company With 18 years of 
  experience in delivering custom software applications, we have 
  the skills, experience, and insight necessary to help our clients’ 
  meet their business objectives'''
h1 = 'Custom Software Development Services'
keyword = 'custom software development'

regex = r"(:|\/|\.|-|\||')"

def clear_s(s):
    cleared_s = (re.sub(regex, ' ', s)).lower()
    return cleared_s

def symbols_count(s):
    return len(s)

def words_count(s):
    cleared_s = clear_s(s)
    l = cleared_s.split(' ')
    return len([s for s in l if s != ''])

def keyword_count(s, key=keyword):
    cleared_s = clear_s(s)
    return cleared_s.count(key)

def keyword_density(s, key=keyword):
    key_count = keyword_count(s, key)
    w_count = words_count(s)
    return f'{round(key_count / w_count * 100)}%'

result = {
    'url': {
        'url_symbols': symbols_count(url),
        'url_words': words_count(url),
        'url_keyword': keyword_count(url),
        'url_key_density': keyword_density(url)
    },
    'title': {
        'title_symbols': symbols_count(title),
        'title_words': words_count(title),
        'title_keyword': keyword_count(title),
        'title_key_density': keyword_density(title)
    },
    'description': {
        'description_symbols': symbols_count(description),
        'description_words': words_count(description),
        'description_keyword': keyword_count(description),
        'description_key_density': keyword_density(description)
    },
    'h1': {
        'h1_symbols': symbols_count(h1),
        'h1_words': words_count(h1),
        'h1_keyword': keyword_count(h1),
        'h1_key_density': keyword_density(h1)
    },
}

pprint(result)
