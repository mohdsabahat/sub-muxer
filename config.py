
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    APP_ID = os.environ.get('APP_ID', None)
    API_HASH = os.environ.get('API_HASH', None)

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
