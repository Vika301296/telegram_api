import os
import requests


def fetch_spacex_last_launch(folder='images', launch_id='latest'):
    launch_url = f'https://api.spacexdata.com/v3/launches/{launch_id}'
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


if __name__ == "__main__":
    fetch_spacex_last_launch()
