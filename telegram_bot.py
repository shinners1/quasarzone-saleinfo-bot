import telepot
import time


class TelegramBot:
    def __init__(self, token, id):
        self.token = token
        self.id = id
        self.bot = telepot.Bot(token)

    def send_html(self, msg):
        self.bot.sendMessage(self.id, msg, parse_mode='html')
        time.sleep(3)
