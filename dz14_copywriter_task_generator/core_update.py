import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from requests_html import HTMLSession
from string import punctuation


COPYWRITER_TASK = '''
Написать текст с заголовком H1 в котором должно 
быть вхождения ключа {keyword}.

Должны быть заголовки H2-H6 c вхождением ключей 
с группы {keywords_main}.

В тексте должны быть такие ключевые слова:
{keywords_main} и {keywords_secondary}.

Нужно проставить внутреннюю перелинковку по ключам
с группы {keywords_main}.

Текст должен быть уникальным на минимум 98%.
Размер текста от 2000 символов.
'''


PORT = 587
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "egor.ivanovvv.2020@gmail.com"
PASSWORD = '8Ng7mbA2sH'


def send_email(message, receiver_email):

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = 'ТЗ для копирайтера'
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    session = smtplib.SMTP(SMTP_SERVER, PORT)
    session.starttls()
    session.login(SENDER_EMAIL, PASSWORD)
    text = msg.as_string()
    session.sendmail(SENDER_EMAIL, receiver_email, text)
    session.quit()

    print('[OK] Email Send')


def google_scraper(keyword, lang='en', serp_count=10):

    with HTMLSession() as session:
        resp = session.get(f'https://www.google.com/search?'
                           f'q={keyword}&num={serp_count}&hl={lang}')

    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')

    return links


def get_text(link):
    print(f'Get text from: {link}')
    with HTMLSession() as session:
        response = session.get(link)
    try:
        description = response.html.xpath(
            '//meta[@name="description"]/@content')[0]
    except IndexError:
        description = ''
    try:
        title = response.html.xpath('//title')[0].text
    except IndexError:
        title = ''
    try:
        h1 = response.html.xpath('//h1')[0].text
    except IndexError:
        h1 = ''
    return description + ' ' + title + ' ' + h1


def texts_analyzer(texts):
    """
    Function that get main keywords and secondary keywords from SERP texts.
    :param texts:
    :return: keywords_main, keywords_secondary - lists
    """

    all_text = ' '.join(texts).lower()

    for sym in punctuation:
        all_text = all_text.replace(sym, ' ').replace('  ', ' ')

    all_keys = all_text.split()
    text_dictionary = dict()

    for key in all_keys:

        if len(key) <= 3:
            continue

        if key not in text_dictionary:
            text_dictionary[key] = 1
        else:
            text_dictionary[key] += 1

    best_10_keys = sorted(text_dictionary.items(),
                          key=lambda x: x[1], reverse=True)[:10]
    best_10_keys = {key[0] for key in best_10_keys}

    return best_10_keys
