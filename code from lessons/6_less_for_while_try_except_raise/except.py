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

my_domain = input('Enter your domain: ')


if '.com' not in my_domain:
    raise ValueError('This is not a domain! Your '
                     'domain should contains .com.')


position = 'Not Found'

try:
    position = domains.index(my_domain) + 1

except Exception as e:
    print('Sh#t happens!', e, type(e))

finally:
    print('All Done!')


print('Website position is:', position)
