import os
import requests

from os.path import splitext, split
from urllib.parse import urlparse, unquote


def get_extension(url):
    split_url = urlparse(url)
    path_without_encoding = unquote(split_url.path)
    filename = split(path_without_encoding)
    extension = (splitext(filename[1]))[1]
    return extension


def download_picture(
        folder, number, picture_extension,
        prefix, picture_url, payload=None):
    response = requests.get(picture_url, params=payload)
    response.raise_for_status()
    filename = os.path.join(
        folder, f'{prefix}_picture_{number}{picture_extension}')
    with open(filename, 'wb') as file:
        file.write(response.content)
