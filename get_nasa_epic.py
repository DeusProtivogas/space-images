import argparse
import os
import datetime
import requests
from dotenv import load_dotenv


def get_nasa_epic(path, api_key, count=2):
    params = {
        "api_key": api_key,
    }
    today_date = datetime.date.today()
    yesterday_date = today_date - datetime.timedelta(days=3)

    url_epic = f"https://api.nasa.gov/EPIC/api/natural/" \
               f"date/{yesterday_date.strftime('%Y-%m-%d')}"
    response = requests.get(url_epic, params=params)
    response.raise_for_status()

    for index, item in enumerate(response.json()):
        if index >= int(count):
            break
        id = item.get("identifier")
        url_image = f"https://api.nasa.gov/EPIC/archive/natural" \
                    f"/{yesterday_date.strftime('%Y/%m/%d')}/" \
                    f"png/epic_1b_{id}.png"

        response_image = requests.get(url_image, params=params)
        response_image.raise_for_status()

        image_path = f"{path}nasa_epic_{index}.png"
        with open(image_path, 'wb') as file:
            file.write(response_image.content)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    parser = argparse.ArgumentParser(description='Download NASA EPIC images: ')
    parser.add_argument('-c', '--count', help='Number of images')
    args = parser.parse_args()

    path = "images/"

    get_nasa_epic(path, api_key, args.count)
