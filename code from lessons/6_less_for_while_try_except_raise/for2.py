domains = [
    'buyessayfriend.com',
    'payforessay.net',
    'buyessayclub.com',
    'essayshark.com',
    'www.wiseessays.com',
    'justbuyessay.com',
    'www.customwritings.com',
    'academized.com',
    'buyessayonline.org',
    'buyessay.net',
    'papernow.org',
    'ibuyessay.com',
    'buyessay.co.uk',
    'buyessay.org',
    'ukwritings.com',
    'www.masterpapers.com',
    'edubirdie.com',
    'grademiners.com',
    'www.ultius.com',
    'samedayessay.com',
    'australianhelp.com',
    'ukessay.com',
    'bestessay4u.com',
    'essays24.org',
    'waywrite.com',
    'essayyoda.com',
    'royalessays.co.uk',
    'www.affordable-papers.net',
    'writemyessay.services',
    'www.privatewriting.com',
    'www.npr.org'
]


# my_domain = 'buyessay.org'
#
# position = 'Not found'
#
# for i, dm in enumerate(domains, start=1):
#     if dm == my_domain:
#         position = i
#         break
#
# # position = domains.index(my_domain) + 1
# print('Website position is:', position)



# url_results1 = []
# base_url = 'https://moz.com/blog'
# max_page = 387
# for i in range(2, max_page):
#     url = base_url + f'?page={i}'
#     url_results1.append(url)
#
#
# url_results2 = [base_url + f'?page={i}' for i in range(2, 10)]
#
# # print(url_results1)
# print(url_results2)


url_results1 = []
base_url = 'https://moz.com/blog'
max_page = 10
for i in range(2, max_page):
    url = base_url + f'?page={i}'
    if i % 3 == 0:
        url_results1.append(url)


url_results2 = [base_url + f'?page={i}' for i in range(2, max_page) if i % 3 == 0]

print(url_results1)
print(url_results2)
