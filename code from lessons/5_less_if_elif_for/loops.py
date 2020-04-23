from pprint import pprint


keywords = '''
write my essay
essay writing service
essayyoda
buyessayclub
pay for essay
essay help
essay shark
masterpapers
'''.strip().split('\n')


cities = {
    'london': 10,
    'kyiv': 15,
    'varshava': 20,
    'berlin': 50
}

# keywords[0] = keywords[0] + ' uk'
# keywords[1] = keywords[1] + ' uk'
# keywords[2] = keywords[2] + ' uk'
# keywords[3] = keywords[3] + ' uk'
# keywords[4] = keywords[4] + ' uk'
# keywords[5] = keywords[5] + ' uk'


uk_keywords = []

dict_results = {}

for item in keywords:

    if not (('essay ' in item) or (' essay' in item)):
        continue

    for city in cities:
        val = cities[city]
        new_key = f'{item} {city} {val}'
        # uk_keywords.append(new_key)

        if val in dict_results:
            dict_results[val].append(new_key)
        else:
            dict_results[val] = [new_key]


base_url = 'https://moz.com/blog'
url_results = []
max_page = 387


for i in range(2, max_page):
    url = base_url + f'?page={i}'
    url_results.append(url)


pprint(dict_results)
