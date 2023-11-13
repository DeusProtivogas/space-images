import os
from dotenv import load_dotenv
from pathlib import Path

from download_image_util import download_image
from fetch_spacex_images import fetch_spacex_launch
from get_nasa_apod import get_nasa_apod
from get_nasa_epic import get_nasa_epic


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    path_to_images = "images/"
    Path(path_to_images).mkdir(parents=True, exist_ok=True)

    filename = f'{path_to_images}hubble.jpeg'
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(url, filename)

    fetch_spacex_launch(path_to_images, id="5eb87d47ffd86e000604b38a")

    get_nasa_apod(path_to_images, api_key)

    get_nasa_epic(path_to_images, api_key)


if __name__ == "__main__":
    main()
