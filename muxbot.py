
# (c) mohdsabahat

import logging
logging.basicConfig(level = logging.DEBUG,
                     format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")

logger = logging.getLogger(__name__)

import os

from config import Config

from helper_func.dbhelper import Database as Db
db = Db().setup()

import pyrogram
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)

    plugins = dict(root='plugins')

    app = pyrogram.Client(
        'Subtitle Muxer',
        bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID,
        api_hash = Config.API_HASH,
        plugins = plugins
    )
    app.run()
