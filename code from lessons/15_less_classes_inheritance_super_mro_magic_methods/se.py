from abc import ABCMeta, abstractmethod
from requests_html import HTMLSession


#################################################################

class SearchEngine(metaclass=ABCMeta):

    def __init__(self, num_results, lang):
        self.session = HTMLSession()
        self.url = self.set_url()
        self.xpath = self.set_xpath()

    def crawl_url(self, url):
        response = self.session.get(url)
        links = response.html.xpath(self.xpath)
        return links

    def parse(self, keyword):
        url = self.url.format(keyword)
        return self.crawl_url(url)

    @abstractmethod
    def set_url(self):
        pass

    @abstractmethod
    def set_xpath(self):
        pass


#################################################################

class GoogleSERP(SearchEngine):

    def set_url(self):
        return 'https://www.google.com/search?num=10&hl=en&q={}'

    def set_xpath(self):
        return '//div[@class="r"]/a[1]/@href'


#################################################################

class BingSERP(SearchEngine):

    def set_url(self):
        return 'https://www.bing.com/search?count=10&q={}'

    def set_xpath(self):
        return 'https://www.google.com/search?num=10&hl=en&q={}'


if __name__ == '__main__':

    goo1 = GoogleSERP(10, 'en')

    links = goo1.parse('buy laptop')

    print(links)
