import os
import requests

from dotenv import load_dotenv
from pictures import get_extension, download_picture


def get_apod_pictures(count=1, folder='images'):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': api_key,
        'count': count}
    apod_pictures = requests.get(apod_url, params=payload)
    apod_pictures.raise_for_status()
    apod_pictures = apod_pictures.json()
    for number, apod_picture in enumerate(apod_pictures):
        picture_url = apod_picture['url']
        picture_extension = get_extension(picture_url)
        prefix = 'apod'
        download_picture(
            folder, number, picture_extension, prefix, picture_url)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    get_apod_pictures()
