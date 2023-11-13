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
    print(args.pause)

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = "@space_images_devman"

    bot = telegram.Bot(token=bot_token)


    # print(bot.get_me())

    # bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    # bot.send_document(chat_id=chat_id, document=open('images/spacex_0.jpeg', 'rb'))
    # for _, _, item in os.walk("images"):
    #     print(item)
    #     print("AAA")
    images = list(os.walk("images"))[0][2]

    while True:
        random.shuffle(images)
        for image in images:
            bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
            time.sleep(args.pause)


