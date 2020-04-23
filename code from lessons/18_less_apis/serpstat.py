from requests_html import HTMLSession


url = 'api.serpstat.com/v3'
token = '29d9199f862fe163f26150af378af89e'
page_size = 10
page = 1
se = 'g_ua'
api_method = 'domain_info'
domain = 'py4you.com'


query = f'http://{url}/{api_method}?' \
        f'query={domain}&token={token}&se={se}&page_size={page_size}'


with HTMLSession() as session:
    response = session.get(query)


breakpoint()
