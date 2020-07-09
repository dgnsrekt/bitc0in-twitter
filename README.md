# bitc0in-twitter
Sync your twitter profile with bitcoin's volatility.

[![Build Status](https://travis-ci.com/dgnsrekt/bitc0in-twitter.svg?branch=master)](https://travis-ci.com/dgnsrekt/bitc0in-twitter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CodeFactor](https://www.codefactor.io/repository/github/dgnsrekt/bitc0in-twitter/badge)](https://www.codefactor.io/repository/github/dgnsrekt/bitc0in-twitter)


```
 /$$$$$$$  /$$$$$$ /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$
| $$__  $$|_  $$_/|__  $$__/ /$$__  $$ /$$$_  $$|_  $$_/| $$$ | $$
| $$  \ $$  | $$     | $$   | $$  \__/| $$$$\ $$  | $$  | $$$$| $$
| $$$$$$$   | $$     | $$   | $$      | $$ $$ $$  | $$  | $$ $$ $$
| $$__  $$  | $$     | $$   | $$      | $$\ $$$$  | $$  | $$  $$$$
| $$  \ $$  | $$     | $$   | $$    $$| $$ \ $$$  | $$  | $$\  $$$
| $$$$$$$/ /$$$$$$   | $$   |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$
|_______/ |______/   |__/    \______/  \______/ |______/|__/  \__/
       /$$$$$$$$ /$$      /$$ /$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$
      |__  $$__/| $$  /$ | $$|_  $$_/|__  $$__/|__  $$__/| $$_____/| $$__  $$
         | $$   | $$ /$$$| $$  | $$     | $$      | $$   | $$      | $$  \ $$
         | $$   | $$/$$ $$ $$  | $$     | $$      | $$   | $$$$$   | $$$$$$$/
         | $$   | $$$$_  $$$$  | $$     | $$      | $$   | $$__/   | $$__  $$
         | $$   | $$$/ \  $$$  | $$     | $$      | $$   | $$      | $$  \ $$
         | $$   | $$/   \  $$ /$$$$$$   | $$      | $$   | $$$$$$$$| $$  | $$
         |__/   |__/     \__/|______/   |__/      |__/   |________/|__/  |__/

Usage: bitc0in_twitter [OPTIONS] COMMAND [ARGS]...

  Syncs your twitter profile with bitcoin's volatility.

Options:
  --help  Show this message and exit.

Commands:
  run   Run Program
  test  Tests that all connections work.
```

## QUICK START DOCKER

### Step 1. Clone the repo.
```
$ git clone git@github.com:dgnsrekt/bitc0in-twitter.git
```
---
### Step 2. Copy your [bullish/bearish] banners and profile pictures into the images/banners folder.
The banners must be in .png format. You can name them what ever you want and add as many bullish and bearish versions as you would like. When transiting from bullish and bearish states the bot will randomly choose from each folder. Use the following guides to help you create the correct profile and banner with the appropriate dimensions.

[GUIDE TO BUILDING HEADER PICTURE](https://blog.snappa.com/twitter-header-size/)

[GUIDE FOR BUILDING PROFILE PICTURE](https://blog.photofeeler.com/twitter-profile-picture-size/)

```
images
├── banner
│   ├── bearish
│   │   └── red_banner.png
│   └── bullish
│       └── green_banner.png
└── profile
    ├── bearish
    │   └── red_profile.png
    └── bullish
        └── green_profile.png
```
---
### Step 3. Update twitter profile credentials.
Use the [TWITTER ACCESS TOKENS GUIDE](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html) to create the consumer/access keys and secrets. Make a copy and rename the **secrets_keys_example** file to **secrets_keys**. Add your profiles keys and secret to the file.

```
CONSUMER_KEY=XXXXXXXXXXXXXXXXXXXXXXXXX
CONSUMER_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_KEY=XXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
```
├── bitc0in_twitter
├── docker-compose.yml
├── docker-entrypoint.sh
├── Dockerfile
├── images
├── LICENSE
├── logme.ini
├── MANIFEST.in
├── noxfile.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
├── secret_keys         <<< place keys/secrets into this file.
├── secret_keys_example <<< copy and rename.
├── settings.ini
├── setup.py
└── tests

```
---
### Step 4. Update the following environmental variables in the docker-compose.yml file.

* CONTROL_PROFILE_IMAGE: [bool] - changes profile pic on price update
* CONTROL_BANNER_IMAGE: [bool] - changes profile banner picture on price update
* CONTROL_PROFILE_COLOR: [bool] - changes profile link color on price update
* CONTROL_PROFILE_DESCRIPTION: [bool] - changes description on price update
* BULLISH_PROFILE_LINK_COLOR: [hex color string] - bullish profile link color
* BEARISH_PROFILE_LINK_COLOR: [hex color string] - bearish profile link color
* BULLISH_PROFILE_DESCRIPTION: [string] - bullish description
* BEARISH_PROFILE_DESCRIPTION: [string] - bearish description
* PROFILE_USERNAME: [string] - the profile username
* MODE: [string] - `run` / `test`
 * `run` mode - starts the bot.
 * `test` mode - allows you to test if the [bullish/bearish] profiles are configured correctly. It will load the bullish profile wait for 15 seconds to allow you to refresh the page and then transition to the bearish state.


TODO: add arrows and bearish example.

![alt text](/docs/images/bullish_profile.png)

#### docker-compose.yml example
```
version: "3.3"
services:
    bitc0in_twitter:
        build: .
        secrets:
            - secret_keys
        environment:
            SECRET_NAME: secret_keys  # Dont touch.
            CONTROL_PROFILE_IMAGE: "True"
            CONTROL_BANNER_IMAGE: "True"
            CONTROL_PROFILE_COLOR: "True"
            CONTROL_PROFILE_DESCRIPTION: "True"
            BULLISH_PROFILE_LINK_COLOR: "#00AA00"
            BEARISH_PROFILE_LINK_COLOR: "#FF001F"
            BULLISH_PROFILE_DESCRIPTION: "TOO THE MOON!!!"
            BEARISH_PROFILE_DESCRIPTION: "BITCOIN IS DEAD AGAIN. :("
            PROFILE_USERNAME: "tester"
            MODE: "run" # run or test mode

secrets:
    secret_keys:
        file: secret_keys

```
---

### Step 5.
```
$ docker-compose up
```

### HEROKU


### DEPENDENCIES
```
[dev-packages]
pytest-watch = "*"
flake8 = "*"
black = "==19.10.b0"

[packages]
ccxt = "*"
tweepy = "*"
schedule = "*"
click = "*"
transitions = "*"
python-decouple = "*"
pillow = "*"
logme = "*"
```

#### TODO
Add JPG format
size information
https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image

https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner

https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload

https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update_with_media

loopkup Tweepy Api._pack_image
rate_limit_status :reference: https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status

Rest api and oauth auth.
