from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from db_frog import Page
from requests_html import HTML
from selenium import webdriver

BAD_PARTS = {'.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi'}

LINKS_QUEUE = Queue()
SCANNED_LINKS = set()


def worker(domain):
    while True:

        url = LINKS_QUEUE.get()
        SCANNED_LINKS.add(url)

        try:
            with webdriver.Chrome(executable_path='./chromedriver') as browser:
                browser.get(url)
                html_code = browser.page_source

        except Exception as e:
            print(e, type(e))
            continue

        html = HTML(html=html_code)

        try:
            page_title = html.xpath('//title')[0].text
        except IndexError:
            page_title = 'Not Found'

        try:
            page_h1 = html.xpath('//h1')[0].text
        except IndexError:
            page_h1 = 'Not Found'

        Page.create(url=url, title=page_title, h1=page_h1)
        print('[OK]', url)

        for link in html.absolute_links:
            link = link.split('#')[0]
            if domain not in link:
                continue
            if link in SCANNED_LINKS:
                continue
            if any(part in link for part in BAD_PARTS):
                continue

            LINKS_QUEUE.put(link)


def main():
    domain = input('Enter domain: ')
    home_page = f'https://{domain}/'
    LINKS_QUEUE.put(home_page)

    threads = 5

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for _ in range(threads):
            executor.submit(worker, domain)


if __name__ == '__main__':
    main()
