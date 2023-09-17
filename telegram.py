import os
import requests

from dotenv import load_dotenv
from os.path import splitext, split
from urllib.parse import urlparse, unquote


load_dotenv()
image_folder = 'images'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
launch_url = 'https://api.spacexdata.com/v3/launches/67'
apod_url = 'https://api.nasa.gov/planetary/apod'
epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'


def fetch_spacex_last_launch(launch_url, folder):
    response = requests.get(launch_url)
    response.raise_for_status()
    response = response.json()
    all_images = response['links']['flickr_images']
    for i, image_url in enumerate(all_images):
        response = requests.get(image_url)
        response.raise_for_status()
        filename = os.path.join(folder, f"picture_{i}.jpg")
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_extension(url):
    split_url = urlparse(url)
    path_without_encoding = unquote(split_url.path)
    filename = split(path_without_encoding)
    extension = (splitext(filename[1]))[1]
    return extension


def get_apod_pictures(apod_url, folder, count):
    payload = {
        'api_key': os.getenv('API_KEY'),
        'count': count}
    apod_pictures = requests.get(apod_url, params=payload)
    apod_pictures.raise_for_status()
    response = apod_pictures.json()
    for i, apod_picture in enumerate(response):
        picture_url = apod_picture['url']
        picture_extension = get_extension(picture_url)
        print(picture_extension)
        response = requests.get(picture_url)
        response.raise_for_status()
        filename = os.path.join(folder, f"nasa_apod_{i}.{picture_extension}")
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_epic_pictures(epic_url, folder):
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
