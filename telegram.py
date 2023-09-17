import os
import requests

from os.path import splitext, split
from urllib.parse import urlparse, unquote

image_folder = 'images'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
# url = "https://example.com/txt/hello%20world.txt?v=9#python"
launch_url = 'https://api.spacexdata.com/v3/launches/67'
apod_url = 'https://api.nasa.gov/planetary/apod'


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
        'api_key': 'YxxmPf67CgZOMvoBPx4eOxXoao6hvveg76fJKykS',
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


print(get_apod_pictures(apod_url, image_folder, 30))
