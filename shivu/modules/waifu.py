#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# For Waifu/Husbando telegram bots.
# Updated and Added new commands, features and style by https://github.com/lovetheticx
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# <============================================== IMPORTS =========================================================>
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from shivu import application
from shivu.state import state

# <================================================ FUNCTIONS =====================================================>
async def get_waifu_data():
    cosplay_url = "https://api.waifu.pics/sfw/waifu"
    response = await state.get(cosplay_url)
    return response.json()


async def cosplay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = await get_waifu_data()
        photo_url = data.get("url")  # Corrected key: "url" instead of "cosplay_url"
        if photo_url:
            await update.message.reply_photo(photo=photo_url)
        else:
            await update.message.reply_text("Could not fetch photo URL.")
    except state.FetchError:
        await update.message.reply_text("Unable to fetch data.")


# <================================================ HANDLER =======================================================>
application.add_handler(CommandHandler("waifu", cosplay, block=False))
