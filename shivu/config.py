class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5675252446"
    sudo_users = "5675252446"
    GROUP_ID = -1001926606886
    TOKEN = "6577035686:AAF_0B2tzjNVgljyQNkTa7G_pSn_lbl3L6A"
    mongo_url = "mongodb+srv://yunyxedits:assalom%4013@waifudata.vfutysm.mongodb.net/?retryWrites=true&w=majority&appName=waifudata"
    PHOTO_URL = ["https://telegra.ph/file/b3d10ca4fb7542b33644f.jpg", "https://telegra.ph/file/2ff11d5cf9fb83a038ed2.jpg", "https://telegra.ph/file/81a90d4eed3e3e2026a78.jpg"]
    SUPPORT_CHAT = "Aniverse_Group"
    UPDATE_CHAT = "Aniverse_Group"
    BOT_USERNAME = "LOVETHETICX_bot"
    CHARA_CHANNEL_ID = "-1001926606886"
    api_id = 29668491
    api_hash = "84feb2e86bc3fa3b0b9bc1e3a3428177"

    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
