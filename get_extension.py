from os.path import splitext, split
from urllib.parse import urlparse, unquote


def get_extension(url):
    split_url = urlparse(url)
    path_without_encoding = unquote(split_url.path)
    filename = split(path_without_encoding)
    extension = (splitext(filename[1]))[1]
    return extension
