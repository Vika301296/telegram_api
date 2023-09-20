import os
import requests

from dotenv import load_dotenv
from pictures import download_picture


def get_epic_pictures(folder='images'):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': api_key}
    pictures = requests.get(epic_url, params=payload)
    pictures.raise_for_status()
    for number, picture in enumerate(pictures.json()):
        date = (picture['date']).split()[0].split(sep='-')
        picture_name = picture['image']
        year, month, day = date[0], date[1], date[2]
        picture_url = (
                      f'https://api.nasa.gov/EPIC/archive/natural/'
                      f'{year}/{month}/{day}/png/{picture_name}.png'
                    )
        picture_extension = '.png'
        prefix = 'epic'
        download_picture(
            folder, number, picture_extension, prefix, picture_url, payload)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    get_epic_pictures()
