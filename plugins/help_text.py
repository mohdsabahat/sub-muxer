
# (c) mohdsabahat

#Logging
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

import os
import pyrogram
from chat import Chat
from config import Config
logging.getLogger('pyrogram').setLevel(logging.WARNING)


@pyrogram.Client.on_message(pyrogram.filters.command(['help']))
async def help_user(bot, update):

    if str(update.from_user.id) in Config.ALLOWED_USERS:
        await bot.send_message(
            update.chat.id,
            Chat.HELP_TEXT,
            parse_mode = 'html',
            disable_web_page_preview = True,
            reply_to_message_id = update.message_id
        )

    else:

        await bot.send_message(
            update.chat.id,
            Chat.NO_AUTH_USER,
            reply_to_message_id = update.message_id
        )

@pyrogram.Client.on_message(pyrogram.filters.command(['start']))
async def start(bot, update):

    if str(update.from_user.id) not in Config.ALLOWED_USERS:
        return await bot.send_message(
            update.chat.id,
            Chat.NO_AUTH_USER,
            reply_to_message_id = update.message_id
        )

    await bot.send_message(
        chat_id = update.chat.id,
        text = Chat.START_TEXT,
        reply_to_message_id = update.message_id
    )
