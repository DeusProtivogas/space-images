import os
import requests
from urllib.parse import urlsplit
from pathlib import Path


def get_file_extension(url):
    url_parsed = urlsplit(url)
    return os.path.splitext( os.path.split(url_parsed.path)[1] )[1]

def download_image(url, path):
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    path_to_images = "images/"
    Path(path_to_images).mkdir(parents=True, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)
