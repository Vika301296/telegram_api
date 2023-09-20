import os
import random
import telegram
import time

from dotenv import load_dotenv


TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
SLEEPING_TIME = 4*60*60


def main():
    images = os.listdir('images')
    load_dotenv()
    bot = telegram.Bot(token=TOKEN)
    last_sent_index = 0
    while True:
        next_images = images[last_sent_index:last_sent_index + 2]
        for image_name in next_images:
            image_path = os.path.join('images', image_name)
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_file)
                last_sent_index += 1
        time.sleep(SLEEPING_TIME)
        last_sent_index += 2
        if last_sent_index >= len(images):
            print('All images have been sent.')
            random.shuffle(images)
            last_sent_index = 0


if __name__ == '__main__':
    main()
