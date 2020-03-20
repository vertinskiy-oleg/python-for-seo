from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('https://www.bing.com/translator')

input_form = browser.find_element_by_id("tta_input_ta")
input_form.send_keys("hello world")
sleep(2)
select_el = Select(browser.find_element_by_id('tta_tgtsl'))
select_el.select_by_value('de')
sleep(2)
output_text = browser.find_element_by_id("tta_output_ta").get_attribute('value')
print(output_text)

with open('translated.txt', 'w') as f:
    f.write(output_text)
