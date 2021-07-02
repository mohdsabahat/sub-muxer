
class Chat:

    START_TEXT = """This is a Telegram Bot to Mux subtitle into a video

<b>Send me a Telegram file to begin</b>

/help for more details..

Credits :- @mohdsabahat
    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Welcome to the Help Menu</b>

1.) Send a Video file or url.
2.) Send a subtitle file (ass or srt)
3.) Choose you desired type of muxing!

To give custom name to file send it with url seperated with |
<i>url|custom_name.mp4</i>

<b>Note : </b><i>Please note that only english type fonts are supported in hardmux other scripts will be shown as empty blocks on the video!</i>

<a href="https://github.com/mohdsabahat/sub-muxer">Repo URL</a>"""

    NO_AUTH_USER = "You are not authorised to use this bot.\nContact the bot owner!"
    DOWNLOAD_SUCCESS = """File downloaded successfully!

Time taken : {} seconds."""
    FILE_SIZE_ERROR = "ERROR : Cannot Extract File Size from URL!"
    MAX_FILE_SIZE = "File size is greater than 2Gb. Which is the limit imposed by telegram!"
    LONG_CUS_FILENAME = """Filename you provided is greater than 60 characters.
Please provide a shorter name."""
    UNSUPPORTED_FORMAT = "ERROR : File format {} Not supported!"
