from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26426018")
    API_HASH = environ.get("API_HASH", "db3addaeb6a7d9a1c8c4d5be80f68d8f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7255526540:AAHr9ywX-k8QlG_fEv8n0wRLczwcKqnGYqI") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Om2323705:9yAxZzAOZm9kw1f6@cluster0.bduwozx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0mongodb+srv://Om2323705:oHu6KwfZ2Re7jGmf@cluster0.bduwozx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6074862505').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
