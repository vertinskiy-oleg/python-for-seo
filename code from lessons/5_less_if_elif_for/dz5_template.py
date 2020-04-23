from requests_html import HTMLSession


url = input('Enter URL: ')
keyword = input('Enter Keyword: ')


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

print('*'*50)
print('TITLE:', title)
print('*'*50)
print('DESCRIPTION:', description)
print('*'*50)
print('H1:', h1)
print('*'*50)


# Ваш код домашнего задания писать тут...


print('\nSEO Page Quality is: XX')
