import requests
import argparse

from download_image_util import download_image


def get_spacex_images(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.json().get("links").get("flickr").get("original")


def fetch_spacex_launch(path, launch_id):
    spacex_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"

    links = get_spacex_images(spacex_url)
    for link_index, link in enumerate(links):
        download_image(link, f"{path}spacex_{link_index}.jpeg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download SpaceX images: ')
    parser.add_argument('-i', '--id', default='latest', help='Launch id')
    args = parser.parse_args()

    path = "images/"

    fetch_spacex_launch(path, args.id)
