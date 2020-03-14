from time import time
from requests_html import HTMLSession


class Crawler:
    def __init__(self, domain=None):
        self.domain = domain
        if domain is None:
            self.domain = input('Enter a domain to crawl: ')
        self.crawled_links = set()
        self.links_to_crawl = set()
        self.file_results = 'checking_results.txt'
        self.session = HTMLSession()
        self.agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    def run(self):
        first_link = f'https://{self.domain}/'
        headers = {'User-Agent': self.agent}
        self.links_to_crawl.add(first_link)

        while True:
            try:
                if len(self.links_to_crawl) == 0:
                    break
                url = self.links_to_crawl.pop()
                t1 = time()
                response = self.session.get(url, headers=headers)
                t2 = time()
                self.crawled_links.add(url)
                bad_parts = ['cdn-cgi', '.jpg', '.gif']

                for link in response.html.absolute_links:
                    if self.domain not in link:
                        continue
                    if any(x in link for x in bad_parts):
                        continue
                    if link in self.crawled_links:
                        continue
                    self.links_to_crawl.add(link)

                result = f'[{round(t2 - t1, 2)} sec] [OK] {url}'
                print(result)

                with open(self.file_results, 'a') as f:
                    f.write(result + '\n')
                    f.flush()

            except KeyboardInterrupt:
                exit()


if __name__ == '__main__':
    craw = Crawler()
    craw.run()


