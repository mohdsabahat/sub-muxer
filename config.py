
import os

class Config:

    BOT_TOKEN = os.environ.get('1943845080:AAHLsLZi6CM_0izDkfFuPtM2MwVRNU5euEs', None)
    APP_ID = os.environ.get( 7069146 , None)
    API_HASH = os.environ.get(' 7f98778e1b3770043d2392c12185a686 ', None)

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('1098504493', ' 7069146 ').split(',')]

    DOWNLOAD_DIR = 'downloads'
