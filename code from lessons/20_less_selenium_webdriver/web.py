import os
from time import sleep
from selenium import webdriver


path = os.path.join(os.getcwd(), 'chromedriver')

SENDER_EMAIL = "egor.ivanovvv.2020@gmail.com"
PASSWORD = '8Ng7mbA2sH'

UA = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'


def browser_google_parser(keyword):
    browser = webdriver.Chrome(executable_path=path)
    browser.get('https://google.com/')
    sleep(2)
    search_input_tag = browser.find_element_by_name('q')
    search_input_tag.send_keys(keyword)
    sleep(2)
    search_button = browser.find_element_by_name('btnK')
    search_button.click()
    sleep(2)
    link_elements = browser.find_elements_by_xpath('//div[@class="r"]/a')
    links = [elem.get_attribute('href') for elem in link_elements]
    return links


def go_to_gmail():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ['enable-automation'])
    chrome_options.add_argument(f'user-agent={UA}')

    browser = webdriver.Chrome(executable_path=path, options=chrome_options)
    browser.set_window_size(1366, 768)

    browser.get('https://google.com/')
    sleep(1)

    login_but = browser.find_element_by_id('gb_70')
    login_but.click()

    sleep(3)

    mail_field = browser.find_element_by_name('identifier')
    mail_field.send_keys(SENDER_EMAIL)

    sleep(2.4)

    button_next = browser.find_element_by_id('identifierNext')
    button_next.click()

    sleep(1.7)

    pass_field = browser.find_element_by_name('password')
    pass_field.send_keys(PASSWORD)

    sleep(4.6)

    button_next = browser.find_element_by_id('passwordNext')
    button_next.click()

    breakpoint()


def get_web_page(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ['enable-automation'])
    chrome_options.add_argument(f'user-agent={UA}')
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=path, options=chrome_options)
    browser.set_window_size(1366, 768)
    browser.get(url)
    sleep(7)
    html_code = browser.page_source
    browser.close()
    browser.quit()
    return html_code


if __name__ == '__main__':
    # url = 'https://www.olx.ua/obyavlenie/avtokreslo-0-stokke-izi-go-modular-by-besafe-IDHoCXV.html'
    # code = get_web_page(url)
    # print(code)
    go_to_gmail()
