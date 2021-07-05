
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', "1866535617:AAH6dQwIV9iHXuVJ4rHNwmOiQUvSsTQjSwE")
    APP_ID = os.environ.get('APP_ID', "1760604")
    API_HASH = os.environ.get('API_HASH', "bfa3e9ea66d4c8cc1da1471b516c2b10")

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
