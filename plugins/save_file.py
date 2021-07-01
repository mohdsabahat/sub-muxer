import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
import time
from chat import Chat
from config import Config
from pyrogram import Client, filters
from helper_func.progress_bar import progress_bar
from helper_func.dbhelper import Database as Db

db = Db()

async def _check_user(filt, c, m):
    chat_id = str(m.from_user.id)
    if chat_id in Config.ALLOWED_USERS:
        return True
    else :
        return False

check_user = filters.create(_check_user)

@Client.on_message(filters.document & check_user & filters.private)
async def save_doc(client, message):

    chat_id = message.from_user.id
    start_time = time.time()
    downloading = await client.send_message(chat_id, 'Downloading your File!')
    download_location = await client.download_media(
        message = message,
        file_name = Config.DOWNLOAD_DIR+'/',
        progress = progress_bar,
        progress_args = (
            'Initializing',
            downloading,
            start_time
        )
    )

    if download_location is None:
        return client.edit_message_text(
            text = 'Downloading Failed!',
            chat_id = chat_id,
            message_id = downloading.message_id
        )

    await client.edit_message_text(
        text = Chat.DOWNLOAD_SUCCESS.format(time.time()-start_time),
        chat_id = chat_id,
        message_id = downloading.message_id
    )

    tg_filename = os.path.basename(download_location)
    try:
        og_filename = message.document.filename
    except:
        og_filename = False

    if og_filename:
        #os.rename(Config.DOWNLOAD_DIR+'/'+tg_filename,Config.DOWNLOAD_DIR+'/'+og_filename)
        save_filename = og_filename
    else :
        save_filename = tg_filename

    ext = save_filename.split('.').pop()
    filename = str(round(start_time))+'.'+ext

    if ext in ['srt','ass']:
        os.rename(Config.DOWNLOAD_DIR+'/'+tg_filename,Config.DOWNLOAD_DIR+'/'+filename)
        db.put_sub(chat_id, filename)
        if db.check_video(chat_id):
            text = 'Subtitle file downloaded successfully.\nChoose your desired muxing!\n[ /softmux , /hardmux ]'
        else:
            text = 'Subtitle file downloaded.\nNow send Video File!'

        await client.edit_message_text(
            text = text,
            chat_id = chat_id,
            message_id = downloading.message_id
        )

    elif ext in ['mp4','mkv']:
        os.rename(Config.DOWNLOAD_DIR+'/'+tg_filename,Config.DOWNLOAD_DIR+'/'+filename)
        db.put_video(chat_id, filename, save_filename)
        if db.check_sub(chat_id):
            text = 'Video file downloaded successfully.\nChoose your desired muxing.\n[ /softmux , /hardmux ]'
        else :
            text = 'Video file downloaded successfully.\nNow send Subtitle file!'
        await client.edit_message_text(
            text = text,
            chat_id = chat_id,
            message_id = downloading.message_id
        )

    else:
        text = f'File extension ("{ext}") not supported!\nFile = {filename}'
        await client.edit_message_text(
            text = text,
            chat_id = chat_id,
            message_id = downloading.message_id
        )
        os.remove(Config.DOWNLOAD_DIR+'/'+filename)


@Client.on_message(filters.video & check_user & filters.private)
async def save_video(client, message):

    chat_id = message.from_user.id
    start_time = time.time()
    downloading = await client.send_message(chat_id, 'Downloading your File!')
    download_location = await client.download_media(
        message = message,
        file_name = Config.DOWNLOAD_DIR+'/',
        progress = progress_bar,
        progress_args = (
            'Initializing',
            downloading,
            start_time
            )
        )

    if download_location is None:
        return client.edit_message_text(
            text = 'Downloading Failed!',
            chat_id = chat_id,
            message_id = downloading.message_id
        )

    tg_filename = os.path.basename(download_location)
    try:
        og_filename = message.document.filename
    except:
        og_filename = False
    
    if og_filename:
        save_filename = og_filename
    else :
        save_filename = tg_filename
    
    ext = save_filename.split('.').pop()
    filename = str(round(start_time))+'.'+ext
    os.rename(Config.DOWNLOAD_DIR+'/'+tg_filename,Config.DOWNLOAD_DIR+'/'+filename)
    
    db.put_video(chat_id, filename, save_filename)
    if db.check_sub(chat_id):
        text = 'Video file downloaded successfully.\nChoose your desired muxing.\n[ /softmux , /hardmux ]'
    else :
        text = 'Video file downloaded successfully.\nNow send Subtitle file!'
    await client.edit_message_text(
            text = text,
            chat_id = chat_id,
            message_id = downloading.message_id
            )
