from telegram_bot import *
import urllib.request
import urllib.parse
import ssl
import bs4
import datetime


def check_saleinfo_and_send_alarm(bot):
    url = 'https://quasarzone.co.kr/bbs/qb_saleinfo'
    prefix = 'https://quasarzone.co.kr'

    with urllib.request.urlopen(url, context=CONTEXT) as response:
        html = response.read()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        table = soup.find('div', class_='market-type-list market-info-type-list relative')
        posts = table.find_all('a', class_='subject-link')

        for p in posts:
            title = p.text.strip()
            href = p['href']
            url = prefix + href
        
            if title != BLIND_MESSAGE:
                date, details = get_post_content(url)
                posting_time = datetime.datetime.strptime(date, '%Y.%m.%d %H:%M')

                if (executed_time - posting_time) > datetime.timedelta(minutes=CHECK_INTERVAL_MIN):
                    break
                
                html_str = generate_html(title, url, date, details)
                bot.send_html(html_str)
                print(html_str)


def get_post_content(url):
    with urllib.request.urlopen(url, context=CONTEXT) as response:
        html = response.read()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        date = soup.find('span', class_='date').text.strip()
        post_table = soup.find('table')
        tags = list(map(lambda x: x.text.strip(), post_table.find_all("th")))
        values = list(map(lambda x: x.text.strip(), post_table.find_all('td')))
        details = dict(zip(tags, values))

        return date, details


def generate_html(title, url, date, details):
    ret = f"<b>게시글\t</b>\t{title}\n"
    ret += f"<b>게시일</b>\t{date}\n\n"

    link = None
    no_price = False

    for tag in details:
        if details[tag] == "":
            continue
        elif details[tag] == NO_PRICE_STRING:
            no_price = True
            continue
        elif tag == "배송비/직배" and no_price:
            continue

        if tag == "링크":
            link = f"<a href =\"{details[tag]}\">구매 링크 바로가기</a>\n"
        else:
            ret += f"{tag} : {details[tag]}\n"

    ret += "\n"

    if link is not None : ret += link
    ret += f"<a href =\"{url}\">퀘이사존 링크 바로가기</a>\n"

    return ret


CONTEXT = ssl._create_unverified_context()
BLIND_MESSAGE = '블라인드 처리된 글입니다.'
NO_PRICE_STRING = '￦ 0 (KRW)'
CHECK_INTERVAL_MIN = 10

telegram_bot_id = ''
telegram_bot_token = ''
telegram_bot = TelegramBot(token=telegram_bot_token, id=telegram_bot_id)

while True:
    executed_time = datetime.datetime.now()
    check_saleinfo_and_send_alarm(telegram_bot)
    print(executed_time)

    time.sleep(CHECK_INTERVAL_MIN * 60)
