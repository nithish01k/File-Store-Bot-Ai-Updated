import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "24921874"))
  API_HASH = os.environ.get("API_HASH", "0aed607bea6fe6e021cb99394848e5e4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6925894836:AAFLX4dB-cmMjszC_G7mJ5GQsauFhfdJtgw")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "public_file_store_ibot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002112181719"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "api.shareus.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "spwtACrO5uZiyFDRORTLgPRcsqL2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5048991005"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://test123:test123@cluster0.ypzcfxf.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001986933012")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002043543122"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
  <b>
╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔹 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
├🔹 Language: [Python 3](https://www.python.org)
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
├🔸 Bᴜʏ Tʜɪs Bᴏᴛ: [Click Here](https://t.me/sonali_sahaibot)
╰──────────[ 🤍 ]───────────⍟
</b>
"""
  ABOUT_DEV_TEXT = f"""
<b>𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [˹ᴍɪss sonali ♡゙ ˼](https://t.me/sonali_sahaibot)
<b>Aʟʟ Bᴏᴛs Lɪsᴛ: [Click Here](https://t.me/sonali_sahaibot)
</b>
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
