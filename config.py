# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28814392")
    API_HASH = environ.get("API_HASH", "38d09c28822aa20a56c43c4b492efba6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7883921930:AAFKqi3sSe_auhw1FlpSEGeoUmnRes0CdCM") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7228509851').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ramsaranhero1:EMVwKybGR1lBF5DZ@cluster0.tst47tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ramsaranhero1")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '2570268731'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "Flase")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
