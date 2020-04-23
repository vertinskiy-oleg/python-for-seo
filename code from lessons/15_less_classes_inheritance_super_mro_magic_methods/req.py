from requests_html import HTMLSession


class MyOwnSession(HTMLSession):

    def get(self, url, **kwargs):
        resp = super().get(url, **kwargs)
        title = resp.html.xpath('//title')[0].text
        return title


url1 = 'https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance'

session = MyOwnSession()

result = session.get(url1)

print(result)
