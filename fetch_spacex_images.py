import requests

from pictures import download_picture


def fetch_spacex_last_launch(folder='images', launch_id='latest'):
    launch_url = f'https://api.spacexdata.com/v3/launches/{launch_id}'
    response = requests.get(launch_url)
    response.raise_for_status()
    response = response.json()
    all_images = response['links']['flickr_images']
    for item, image_url in enumerate(all_images):
        response = requests.get(image_url)
        response.raise_for_status()
        picture_extension = '.jpg'
        prefix = 'spacex'
        download_picture(folder, item, picture_extension, response, prefix)


if __name__ == '__main__':
    fetch_spacex_last_launch()
