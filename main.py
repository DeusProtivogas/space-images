import requests
import os
import datetime
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit

from download_image_util import download_image
from fetch_spacex_images import fetch_spacex_launch
from get_nasa_apod import get_nasa_apod
from get_nasa_epic import get_nasa_epic


#
# def get_nasa_epic(path, api_key, count=2):
#     params = {
#         "api_key": api_key,
#         }
#     today_date = datetime.date.today()
#     yesterday_date = today_date - datetime.timedelta(days=3)
#
#     url_epic = f"https://api.nasa.gov/EPIC/api/natural/date/{yesterday_date.strftime('%Y-%m-%d')}"
#     # print(url_epic)
#     response = requests.get(url_epic, params=params)
#     response.raise_for_status()
#
#     images = []
#     for index, item in enumerate(response.json()):
#         if index >= count:
#             break
#         id = item.get("identifier")
#         url_image = f"https://api.nasa.gov/EPIC/archive/natural/{yesterday_date.strftime('%Y/%m/%d')}/png/epic_1b_{id}.png"
#
#         response_image = requests.get(url_image, params=params)
#         response_image.raise_for_status()
#
#         image_path = f"{path}nasa_epic_{index}.png"
#         with open(image_path, 'wb') as file:
#             file.write(response_image.content)
        
#
# def get_nasa_apod(path, api_key, count=2):
#     params = {
#         "api_key": api_key,
#         "count": count,
#              }
#     url_apod = "https://api.nasa.gov/planetary/apod"
#     response = requests.get(url_apod, params)
#     response.raise_for_status()
#     response = response.json()
#     images = []
#     for item in response:
#         if item.get("media_type") == "image":
#             images.append(item.get("url"))
#
#     for image_index, image in enumerate(images):
#         try:
#             image_path = f"{path}nasa_apod_{image_index}.{get_file_extension(image)}"
#
#             image_response = requests.get(image)
#             image_response.raise_for_status()
#
#             with open(image_path, 'wb') as file:
#                 file.write(image_response.content)
#         except:
#             print("Error with NASA image occured")
#             continue
#
# def get_file_extension(url):
#     url_parsed = urlsplit(url)
#     return os.path.splitext( os.path.split(url_parsed.path)[1] )[1]
    

# def fetch_spacex_last_launch(url, path):
#     links = get_SpaceX_images(url)
#     for link_index, link in enumerate(links):
#         download_image(link, f"{path}spacex_{link_index}.jpeg")
#
# def get_SpaceX_images(url):
#     response = requests.get(url)
#     response.raise_for_status()
#
#     # print(response.json().get("links").get("flickr"))
#
#     return response.json().get("links").get("flickr").get("original")
    
#
# def download_image(url, path):
#     headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
#
#     response = requests.get(url, headers=headers)
#     # print(response.text)
#     response.raise_for_status()
#
#     with open(path, 'wb') as file:
#         file.write(response.content)

def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    path_to_images = "images/"
    Path(path_to_images).mkdir(parents=True, exist_ok=True)

    filename = f'{path_to_images}hubble.jpeg'
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(url, filename)
    
    url_SpaceX = "https://api.spacexdata.com/v5/launches/"
    fetch_spacex_launch(path_to_images, id="5eb87d47ffd86e000604b38a")

    # url = "https://apod.nasa.gov/apod/image/2311/GibbousMoon_Strand_960.jpg"
    # print(get_file_extension(url))

    get_nasa_apod(path_to_images, api_key)

    get_nasa_epic(path_to_images, api_key)

if __name__ == "__main__":
    main()
