# import random
# from time import sleep
# from pprint import pprint
# from requests_html import HTMLSession


# keywords = (
#     'buy essays online',
#     'buy essay',
#     'write my essay',
#     'write history essay'
# )

# session = HTMLSession()


# SERP = {}


# for key in keywords:
#     print(f'Send request to Google: [{key}]')
#     resp = session.get(f'https://www.google.com/search?q={key}&num=100&hl=en')
#     links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
#     SERP[key] = [x.split('/')[2] for x in links if 'http' in x]
#     sleep_seconds = random.randint(1, 10)
#     print(f'Sleep: {sleep_seconds}')
#     sleep(sleep_seconds)


# pprint(SERP)

# Ваш код писать тут...

SERP = {'buy essay': ['buyessayfriend.com',
               'payforessay.net',
               'buyessayclub.com',
               'essayshark.com',
               'www.wiseessays.com',
               'justbuyessay.com',
               'academized.com',
               'www.customwritings.com',
               'buyessay.net',
               'buyessayonline.org'],
 'buy essays online': ['buyessayfriend.com',
                       'payforessay.net',
                       'essayshark.com',
                       'www.wiseessays.com',
                       'academized.com',
                       'buyessayclub.com',
                       'justbuyessay.com',
                       'edubirdie.com',
                       'buyessayonline.org',
                       'www.masterpapers.com'],
 'write history essay': ['alphahistory.com',
                         'www.historytoday.com',
                         'www.wikihow.com',
                         'www.ozessay.com.au',
                         'bookbuilder.cast.org',
                         'writingproject.fas.harvard.edu',
                         'handmadewriting.com',
                         'essaylab.org',
                         'www.aresearchguide.com',
                         'sydney.edu.au'],
 'write my essay': ['papernow.org',
                    'www.essaytyper.com',
                    'writemyessays.net',
                    'edubirdie.com',
                    'samedayessay.com',
                    'academized.com',
                    'essaybot.com',
                    'www.masterpapers.com',
                    'writemyessay4me.org',
                    'domywriting.com']}

domains = [set(l) for l in SERP.values()]

all_domains = sorted(set.union(*domains))
intersect_domains = sorted(set.intersection(*domains))

print(domains)
print(all_domains)
print(intersect_domains)