from selenium import webdriver
# from requests_html import HTML
from concurrent.futures import ThreadPoolExecutor

urls = ['https://www.bing.com/', 'https://www.google.com/', 'https://www.yahoo.com/']


def worker(url):
    with webdriver.Chrome(executable_path='./chromedriver') as browser:
        browser.get(url)


# html_code = browser.page_source
#
# html = HTML(html=html_code)
#
# page_title = html.xpath('//title')[0].text
#
# print(page_title)

thread = 2

for url in urls:

    with ThreadPoolExecutor(max_workers=thread) as executor:
        for _ in range(thread):
            executor.submit(worker, url)
