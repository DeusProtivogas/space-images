import argparse
import os

import requests
from dotenv import load_dotenv

from download_image_util import get_file_extension


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
    for item in response:
        if item.get("media_type") == "image":
            images.append(item.get("url"))

    for image_index, image in enumerate(images):
        try:
            image_path = f"{path}nasa_apod_{image_index}.{get_file_extension(image)}"

            image_response = requests.get(image)
            image_response.raise_for_status()

            with open(image_path, 'wb') as file:
                file.write(image_response.content)
        except:
            print("Error with NASA image occured")
            continue


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    parser = argparse.ArgumentParser(description='Download NASA APOD images: ')
    parser.add_argument('--count', help='Number of images')
    args = parser.parse_args()
    # print(args.id)

    path = "images/"

    get_nasa_apod(path, api_key, args.count)
