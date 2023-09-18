import os
import requests

from dotenv import load_dotenv

load_dotenv()


def get_epic_pictures(folder='images'):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': os.getenv('API_KEY')}
    pictures = requests.get(epic_url, params=payload)
    pictures.raise_for_status()
    for i, picture in enumerate(pictures.json()):
        date = (picture['date']).split()[0].split(sep='-')
        picture_name = picture['image']
        year, month, day = date[0], date[1], date[2]
        picture_url = (
                      f'https://api.nasa.gov/EPIC/archive/natural/'
                      f'{year}/{month}/{day}/png/{picture_name}.png'
                    )
        response = requests.get(picture_url, payload)
        response.raise_for_status()
        filename = os.path.join(folder, f"epic_picture_{i}.png")
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    get_epic_pictures()
