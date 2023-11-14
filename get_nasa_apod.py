import argparse
import os

import requests
from dotenv import load_dotenv

from download_image_util import get_file_extension, download_image


def get_nasa_apod(path, api_key, count=2):
    params = {
        "api_key": api_key,
        "count": count,
    }
    url_apod = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url_apod, params)
    response.raise_for_status()
    response = response.json()
    images = []
    for image in response:
        if image.get("media_type") == "image":
            images.append(image.get("url"))

    for image_index, image in enumerate(images):
        try:
            image_path = f"{path}nasa_apod_{image_index}" \
                         f"{get_file_extension(image)}"

            download_image(image, image_path)
        except requests.ConnectionError:
            print("Error with NASA image occured")
            continue


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    parser = argparse.ArgumentParser(description='Download NASA APOD images: ')
    parser.add_argument('-c', '--count', help='Number of images')
    args = parser.parse_args()

    path = "images/"

    get_nasa_apod(path, api_key, args.count)
