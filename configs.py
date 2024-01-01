import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "24921874"))
  API_HASH = os.environ.get("API_HASH", "0aed607bea6fe6e021cb99394848e5e4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6925894836:AAFLX4dB-cmMjszC_G7mJ5GQsauFhfdJtgw")
  LUFFY_PIC = os.environ.get("LUFFY_PIC", "https://graph.org/file/1c15be412eb886ba1c8e3.jpg")
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
  ABOUT_BOT_TEXT = f"""<b>╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : File Store Bot
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>   
├◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├◈ Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://t.me/missqueenbotx>File Store V3.0.0</a>
╰───────────────⍟ </b> 
"""
  ABOUT_DEV_TEXT = f"""
<b>Hɪ I'M <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a>✨\n
ᴛᴀʟᴋ ᴡɪᴛʜ ᴍᴇ : <a href=https://t.me/sonali_sahaibot>Cʟɪᴄᴋ Hᴇʀᴇ</a>
ᴠɪsɪᴛ ᴍʏ ɢɪᴛʜᴜʙ : <a href=https://github.com/sonali1563>Sᴏɴᴀʟɪ's Gɪᴛʜᴜʙ</a>
ᴍʏ Cʜᴀɴɴᴇʟ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>
ᴍʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotxchat>𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥</a>
</b>
"""
  HOME_TEXT = """
  <b>
Hello, [{}](tg://user?id={}) 🤍\n\n❕ This is a Permanent **FileStore Bot**.

🔉 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ TᴇʟᴇGʀᴀᴍ Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ ᴏʀ Aɴʏ Cᴏᴘʏʀɪɢʜᴛ Cʜᴀɴɴᴇʟ, Tʜᴇɴ Iᴛs Usᴇғᴜʟ ғᴏʀ Dᴀɪʟʏ Usᴀɢᴇ, Yᴏᴜ ᴄᴀɴ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Fɪʟᴇ & I ᴡɪʟʟ Sᴇɴᴅ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴛᴏ Yᴏᴜ & Cʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ Sᴀғᴇ ғʀᴏᴍ CᴏᴘʏRɪɢʜᴛ Iɴғʀɪɴɢᴇᴍᴇɴᴛ Issᴜᴇ.
</b>"""
