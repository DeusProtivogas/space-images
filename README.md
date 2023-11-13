# Space images telegram bot
Simple set of scripts for a telegram bot to download space images form different sources and send them to a telegram bot.

## Image downloading

Can be done by launching

```
python3 main.py
```

to get images from different sources. If need to get images from a specific source, use separate scripts.

### fetch_spacex_images.py

Get images from SpaceX launch, by launch id or from the latest launch.

To get images by id:
```commandline
python3 fetch_spacex_images.py --id {id}
```

Example:
```commandline
python3 fetch_spacex_images.py --id 5eb87d42ffd86e000604b384
```

To get latest launch:
```commandline
python3 fetch_spacex_images.py 
```

### get_nasa_apod.py

Get images of the day from NASA site.

To launch:
```commandline
python3 get_nasa_apod.py --count {number of images}
```

Default value for "number of images" is 2.

Example:
```commandline
python3 get_nasa_apod.py --count 2
```

### get_nasa_epic.py

Get images from NASA EPIC.

To launch:
```commandline
python3 get_nasa_epic.py --count {number of images}
```

Default value for "number of images" is 2.

Example:
```commandline
python3 get_nasa_epic.py --count 2
```

## Telegram bot

### telegram_bot.py

Starts a script that sends downloaded images to a telegram bot at certain intervals (default - 4 hours).

To launch:
```commandline
python3 telegram_bot.py -p {time interval}
```

Example:
```commandline
python3 telegram_bot.py -p 1
```
