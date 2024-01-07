import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21925188"))
  API_HASH = os.environ.get("API_HASH", "f9b377f83f916d783f25d95a2f4e232e")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6814859843:AAG55nbGmyxrLyxB9BVCwW_UaXXpd8r_JDI")
  LUFFY_PIC = os.environ.get("LUFFY_PIC", "https://graph.org/file/1c15be412eb886ba1c8e3.jpg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "filestore_new_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002016822623"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "api.tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "spwtACrO5uZiyFDRORTLgPRcsqL2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5431249569"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://test123:test123@cluster0.ypzcfxf.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001887195187")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001535708255"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""<b>╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/thomas_shelby_0_7>THOMAS</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/tamil_rockerZ_1>ᴄʟɪᴄᴋ ᴍᴇ</a>   
├◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
╰───────────────⍟ </b> 
"""
  ABOUT_DEV_TEXT = f"""
<b>Hɪ I'M <a href=https://t.me/filestore_new_bot>Thomas</a>✨\n
ᴛᴀʟᴋ ᴡɪᴛʜ ᴍᴇ : <a href=https://t.me/thomas_shelby_0_7>Cʟɪᴄᴋ Hᴇʀᴇ</a>
ᴠɪsɪᴛ ᴍʏ ɢɪᴛʜᴜʙ : <a href=https://github.com/Thomasshelby333>Thomas's Gɪᴛʜᴜʙ</a>
ᴍʏ Cʜᴀɴɴᴇʟ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/tamil_rockerZ_1>ᴛᴀᴍɪʟʀᴏᴄᴋᴇʀᴢ</a>
ᴍʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/+xNG8OZGJbMA0MDg1>𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥</a>
</b>
"""
  HOME_TEXT = """<b>
Hello, [{}](tg://user?id={}) 🤍\n
◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.
◈ I Cᴀɴ Gɪᴠᴇ Yᴏᴜ Dɪʀᴇᴄᴛ Aɴᴅ Bᴀᴛᴄʜ Lɪɴᴋs Jᴜsᴛ Fᴏʀᴡᴀʀᴅ Mᴇ Fɪʟᴇs.

• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @missqueenbotx
</b>"""

  Helps_data_test = """<b>
⚪️ Hᴏᴡ ᴛᴏ Usᴇ Bᴏᴛ & ɪᴛ's Bᴇɴᴇғɪᴛs?? 👇

• Sᴇɴᴅ ᴍᴇ ᴀɴʏ Fɪʟᴇ & Iᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ Mʏ Dᴀᴛᴀʙᴀsᴇ & Yᴏᴜ ᴡɪʟʟ Gᴇᴛ ᴛʜᴇ Fɪʟᴇ Lɪɴᴋ.

• Bᴇɴᴇғɪᴛs: Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ TᴇʟᴇGʀᴀᴍ Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ ᴏʀ Aɴʏ Cᴏᴘʏʀɪɢʜᴛ Cʜᴀɴɴᴇʟ, Tʜᴇɴ Iᴛs Usᴇғᴜʟ ғᴏʀ Dᴀɪʟʏ Usᴀɢᴇ, Yᴏᴜ ᴄᴀɴ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Fɪʟᴇ & I ᴡɪʟʟ Sᴇɴᴅ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴛᴏ Yᴏᴜ & Cʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ Sᴀғᴇ ғʀᴏᴍ CᴏᴘʏRɪɢʜᴛ Iɴғʀɪɴɢᴇᴍᴇɴᴛ Issᴜᴇ.

⚪️ ғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ <a href=https://t.me/thomas_shelby_0_7>Thomas</a> : <a href=https://t.me/+xNG8OZGJbMA0MDg1>Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</a>
 </b>"""
