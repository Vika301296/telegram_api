import os
import random
import telegram
import time

from dotenv import load_dotenv


def main():
    images = os.listdir('images')
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    last_sent_index = 0
    while True:
        for index, image_name in enumerate(images):
            image_path = os.path.join('images', image_name)
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_file)
                last_sent_index += 1
                time.sleep(SLEEPING_TIME)
                last_sent_index = index
            if last_sent_index >= len(images):
                print('All images have been sent.')
                random.shuffle(images)
                last_sent_index = 0


if __name__ == '__main__':
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    SLEEPING_TIME = 4*60*60
    main()
