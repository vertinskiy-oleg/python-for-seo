
def get_domain(url):
    """
    Function that get url on input and return domain name from this url.

    :param url: url is string
    :return: domain name as string
    """
    dom = url.split('/')[2]
    if dom.startswith('www.'):
        dom = dom[4:]
    return dom


url = 'https://py4you.com/courses/python-for-seo/'

domain = get_domain(url)

print(domain)
