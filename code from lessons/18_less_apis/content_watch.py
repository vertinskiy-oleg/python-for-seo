from pprint import pprint
from requests_html import HTMLSession


def get_uniquness_of_url(url, ignore):

    api_url = 'https://content-watch.ru/public/api/'

    post_data = {
        'action': 'CHECK_URL',
        'key': 'LaaZxj2RH0vRQDB',
        'ignore': ignore,
        'url': url
    }

    with HTMLSession() as session:
        response = session.post(api_url, data=post_data)

    result = response.json()

    try:
        uniq = result['percent']
    except KeyError:
        uniq = 'undefined'
        print(response.status_code, result)

    return uniq
