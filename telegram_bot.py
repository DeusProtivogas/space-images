import os

import telegram
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = "@space_images_devman"

    bot = telegram.Bot(token=bot_token)
    # print(bot.get_me())

    # bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    bot.send_document(chat_id=chat_id, document=open('images/spacex_0.jpeg', 'rb'))
