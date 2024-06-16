from asyncio import run

import telegram


class TelegramBot:
    def __init__(self):
        self.TOKEN = '7431182722:AAGMQ2zsgzPnG1e-bAn2JGwA7UWLsDELz9Q'
        self.bot = telegram.Bot(token=self.TOKEN)

    def send_message(self, user, message):
        if hasattr(user, 'id_telegram') and user.id_telegram:
            run(self.bot.send_message(user.id_telegram, message))
