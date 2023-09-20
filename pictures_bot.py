import os
import random
import telegram
import time

from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    sleeping_time = 4*60*60
    images = os.listdir('images')
    bot = telegram.Bot(token=telegram_token)
    last_sent_index = 0
    while True:
        for index, image_name in enumerate(images):
            image_path = os.path.join('images', image_name)
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id=telegram_chat_id, photo=image_file)
                last_sent_index += 1
                time.sleep(sleeping_time)
                last_sent_index = index
            if last_sent_index >= len(images):
                print('All images have been sent.')
                random.shuffle(images)
                last_sent_index = 0


if __name__ == '__main__':
    main()
