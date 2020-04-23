from time import sleep
from queue import Queue
from threading import Lock, Thread
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
from db import Page

BAD_PARTS = {'.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi'}

locker = Lock()

LINKS_QUEUE = Queue()
SCANNED_LINKS = set()


def worker(domain):
    while True:

        # if LINKS_QUEUE.qsize() == 0:
        #     sleep(10)
        #     if LINKS_QUEUE.qsize() == 0:
        #         break
        #     continue

        url = LINKS_QUEUE.get()
        SCANNED_LINKS.add(url)

        try:
            with HTMLSession() as session:
                resp = session.get(url)

            assert resp.status_code == 200

        except Exception as e:
            print(e, type(e))
            continue

        try:
            page_title = resp.html.xpath('//title')[0].text
        except IndexError:
            page_title = 'Not Found'

        try:
            page_h1 = resp.html.xpath('//h1')[0].text
        except IndexError:
            page_h1 = 'Not Found'

        Page.create(url=url, title=page_title, h1=page_h1)
        print('[OK]', url)

        with locker:
            with open('results.csv', 'a') as f:
                f.write(f'{url}\t{page_title}\t{page_h1}\n')

        for link in resp.html.absolute_links:
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

    thread = 100
    # with ThreadPoolExecutor(max_workers=thread) as executor:
    #     for _ in range(thread):
    #         executor.submit(worker, domain)

    for _ in range(thread):
        Thread(target=worker, args=(domain,)).start()


if __name__ == '__main__':
    main()
