import requests
import argparse

from download_image_util import download_image


def get_SpaceX_images(url):
    response = requests.get(url)
    response.raise_for_status()

    # print(response.json().get("links").get("flickr"))

    return response.json().get("links").get("flickr").get("original")
def fetch_spacex_launch(path, id):
    if id:
        url_spacex = f"https://api.spacexdata.com/v5/launches/{id}"
    else:
        url_spacex = "https://api.spacexdata.com/v5/launches/latest"

    print(url_spacex)

    links = get_SpaceX_images(url_spacex)
    for link_index, link in enumerate(links):
        download_image(link, f"{path}spacex_{link_index}.jpeg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download SpaceX images: ')
    parser.add_argument('-i', '--id', help='Launch id')
    args = parser.parse_args()
    # print(args.id)

    path = "images/"

    fetch_spacex_launch(path, args.id)
