import json
import os


def get_user_list(config, key):
    with open('{}/MashaRoBot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
  
    TEMP_DOWNLOAD_DIRECTORY = 'None'
    API_ID = "8785365"  # integer value, dont use ""
    API_HASH = "48c1934c1df9da5b218cfc1382be1bdf"
    TOKEN = "5009926984:AAH6fGW5mTa008lr8aRekqJiuMgrz_0IMjw"
    OWNER_ID = 2015913098  
    OWNER_USERNAME = "RISE2BOSSYT"
    SUPPORT_CHAT = 'MOVIES_MOD'
    JOIN_LOGGER = -1001721546513
    EVENT_LOGS =  -1001721546513

    ALLOW_CHATS = "True"
    SQLALCHEMY_DATABASE_URI = 'postgres://yngnattyfkenzt:f331efbc29e95868c445f7e2b9759809ba0c58b85c9c8ed5e08b4923cb7c277f@ec2-174-129-16-183.compute-1.amazonaws.com:5432/d7db1glnrmilkg'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "BfPIa_u9S0RVHmmaKLJM_JKHNoxoYySPzHSK7YfL9yaba216rkwiAOVC5kcYv1Z1"  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "5009926984"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
