import argparse
import os
import random
import time
import telegram
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Launch Telegram Bot: ')
    parser.add_argument('-p', '--pause', nargs='?', const=3600 * 4, type=int, help='Pause between images in seconds')
    args = parser.parse_args()
    if not args.pause:
        args.pause = 3600 * 4

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = "@space_images_devman"

    bot = telegram.Bot(token=bot_token)

    images = list(os.walk("images"))[0][2]

    while True:
        random.shuffle(images)
        for image in images:
            bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
            time.sleep(args.pause)

