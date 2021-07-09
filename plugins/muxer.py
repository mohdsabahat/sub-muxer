from pyrogram import Client, filters
from helper_func.progress_bar import progress_bar
from helper_func.dbhelper import Database as Db
from helper_func.mux import softmux_vid, hardmux_vid
from config import Config
import time
import os

db = Db()

async def _check_user(filt, c, m):
    chat_id = str(m.from_user.id)
    if chat_id in Config.ALLOWED_USERS:
        return True
    else :
        return False

check_user = filters.create(_check_user)

@Client.on_message(filters.command('softmux') & check_user & filters.private)
async def softmux(client, message):

    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'First send a Video File\n'
    if not og_sub_filename :
        text += 'Send a Subtitle File!'

    if not (og_sub_filename and og_vid_filename) :
        await client.send_message(chat_id, text)
        return

    text = 'Your File is Being Soft Subbed. This should be done in few seconds!'
    sent_msg = await client.send_message(chat_id, text)

    softmux_filename = await softmux_vid(og_vid_filename, og_sub_filename, sent_msg)
    if not softmux_filename:
        return

    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+softmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)

    start_time = time.time()
    try:
        await client.send_document(
                chat_id, 
                progress = progress_bar, 
                progress_args = (
                    'Uploading your File!',
                    sent_msg,
                    start_time
                    ), 
                document = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                caption = final_filename
                )
        text = 'File Successfully Uploaded!\nTotal Time taken : {} seconds'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        print(e)
        await client.send_message(chat_id, 'An error occured while uploading the file!\nCheck logs for details of the error!')

    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass

    db.erase(chat_id)


@Client.on_message(filters.command('hardmux') & check_user & filters.private)
async def hardmux(client, message):
    
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'First send a Video File\n'
    if not og_sub_filename :
        text += 'Send a Subtitle File!'
    
    if not (og_sub_filename or og_vid_filename) :
        return await client.send_message(chat_id, text)
    
    text = 'Your File is Being Hard Subbed. This might take a long time!'
    sent_msg = await client.send_message(chat_id, text)

    hardmux_filename = await hardmux_vid(og_vid_filename, og_sub_filename, sent_msg)
    
    if not hardmux_filename:
        return
    
    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+hardmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)
    
    start_time = time.time()
    try:
        await client.send_video(
                chat_id, 
                progress = progress_bar, 
                progress_args = (
                    'Uploading your File!',
                    sent_msg,
                    start_time
                    ), 
                video = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                caption = final_filename
                )
        text = 'File Successfully Uploaded!\nTotal Time taken : {} seconds'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        print(e)
        await client.send_message(chat_id, 'An error occured while uploading the file!\nCheck logs for details of the error!')
    
    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass
    db.erase(chat_id)
