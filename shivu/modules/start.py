#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# For Waifu/Husbando telegram bots.
# Speacial thanks for this amazing repo: https://github.com/MyNameIsShekhar
# Updated and Added new commands, features and style by https://github.com/lovetheticx

# ⊢⊸⊸⊸⊸⊸ New Features ⊸⊸⊸⊸⊸ 
# ⊢ Added Harem Mode                  
# ⊢ Added more buttons for manage harem list
# ⊢ Added pagination for harem list
# ⊢ Updated harem message to new style
# ⊢ Updated max caption length for Harem message
# ⊢ User Friendly functions, easy to understand and use
# ⊢ Added /help as command
# ⊢ And much more...
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


# <============================================== IMPORTS =========================================================>
import random
from html import escape
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler
from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection

# <======================================= START ==================================================>
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        await context.bot.send_message(chat_id=GROUP_ID, text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)}</a>", parse_mode='HTML')
    else:
        if user_data['first_name'] != first_name or user_data['username'] != username:
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    if update.effective_chat.type == "private":
        caption = f"""
**🍃 ɢʀᴇᴇᴛɪɴɢꜱ, ɪ'ᴍ ˹ᴀɴɪᴍᴇ • ɢʀᴀʙʙᴇʀ ワイフ˼ 🫧, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!**
**━━━━━━━▧▣▧━━━━━━━**
⦾ ᴡʜᴀᴛ ɪ ᴅᴏ: ɪ sᴘᴀᴡɴ   
     ᴡᴀɪғᴜs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ғᴏʀ
     ᴜsᴇʀs ᴛᴏ ɢʀᴀʙ.
⦾ ᴛᴏ ᴜsᴇ ᴍᴇ: ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ
     ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀᴘ ᴛʜᴇ ʜᴇʟᴘ
     ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.
**━━━━━━━▧▣▧━━━━━━━**
"""
        keyboard = [
            [InlineKeyboardButton("✣  ᴀᴅᴅ ᴍᴇ  ✣", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("〄  ꜱᴜᴘᴘᴏʀᴛ  〄", url=f'https://t.me/{SUPPORT_CHAT}'), InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇꜱ ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("❖  ʜᴇʟᴘ  ❖", callback_data='help')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='Markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("✣  ᴀᴅᴅ ᴍᴇ  ✣", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("〄  ꜱᴜᴘᴘᴏʀᴛ  〄", url=f'https://t.me/{SUPPORT_CHAT}'), InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇꜱ ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("❖  ʜᴇʟᴘ  ❖", callback_data='help')],
            [InlineKeyboardButton("✣  ꜱᴛᴀʀᴛ ʙᴏᴛ ɪɴ ᴘᴍ  ✣", url=f'http://t.me/{BOT_USERNAME}?start')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption = f"""
🍃 ɢʀᴇᴇᴛɪɴɢꜱ, ɪ'ᴍ ˹ᴀɴɪᴍᴇ • ɢʀᴀʙʙᴇʀ ワイフ˼ 🫧, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!
━━━━━━━▧▣▧━━━━━━━
⦾ ᴡʜᴀᴛ ɪ ᴅᴏ: ɪ sᴘᴀᴡɴ   
     ᴡᴀɪғᴜs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ғᴏʀ
     ᴜsᴇʀs ᴛᴏ ɢʀᴀʙ.
⦾ ᴛᴏ ᴜsᴇ ᴍᴇ: ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ
     ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀᴘ ᴛʜᴇ ʜᴇʟᴘ
     ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.
━━━━━━━▧▣▧━━━━━━━
""", reply_markup=reply_markup)

# <======================================= HELP COMMAND ==================================================>        
async def help(update: Update, context: CallbackContext) -> None:
    help_text = """
    **➲ Below are the commands for users:**

    **━━━━━━━ᴄᴏᴍᴍᴀɴᴅꜱ━━━━━━━**
    ⎆ `/grab` : ᴛᴏ ɢʀᴀʙ ᴀ ᴡᴀɪꜰᴜ
    ⎆ `/harem` : ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ɢʀᴀʙʙᴇᴅ ᴡᴀɪꜰᴜ
    ⎆ `/fav` : ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴡᴀɪꜰᴜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ
    ⎆ `/gift` : ᴛᴏ ɢɪꜰᴛ ᴀ ᴡᴀɪꜰᴜ
    ⎆ `/trade` : ᴛᴏ ᴛʀᴀᴅᴇ ᴡᴀɪꜰᴜꜱ
    ⎆ `/ctop` : ʏᴏᴜʀ ᴄʜᴀᴛᴛᴏᴘ ɢʀᴀʙʙᴇʀꜱ
    ⎆ `/changetime` : ᴄʜᴀɴɢᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ (ᴏɴʟʏ ᴡᴏʀᴋꜱ ɪɴ ɢʀᴏᴜᴘꜱ)
    ⎆ `/top` : ᴛᴏ ꜱᴇᴇ ᴛᴏᴘ ɢʀᴀʙʙᴇʀꜱ
    **━━━━━━━ᴄᴏᴍᴍᴀɴᴅꜱ━━━━━━━**
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text, parse_mode='Markdown')

# <======================================= HELP BUTTON ==================================================>
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
**➲ Below are the commands for users:**

**━━━━━━━ᴄᴏᴍᴍᴀɴᴅꜱ━━━━━━━**
⎆ `/grab` : ᴛᴏ ɢʀᴀʙ ᴀ ᴡᴀɪꜰᴜ
⎆ `/harem` : ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ɢʀᴀʙʙᴇᴅ ᴡᴀɪꜰᴜ
⎆ `/fav` : ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴡᴀɪꜰᴜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ
⎆ `/gift` : ᴛᴏ ɢɪꜰᴛ ᴀ ᴡᴀɪꜰᴜ
⎆ `/trade` : ᴛᴏ ᴛʀᴀᴅᴇ ᴡᴀɪꜰᴜꜱ
⎆ `/ctop` : ʏᴏᴜʀ ᴄʜᴀᴛᴛᴏᴘ ɢʀᴀʙʙᴇʀꜱ
⎆ `/changetime` : ᴄʜᴀɴɢᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ (ᴏɴʟʏ ᴡᴏʀᴋꜱ ɪɴ ɢʀᴏᴜᴘꜱ)
⎆ `/top` : ᴛᴏ ꜱᴇᴇ ᴛᴏᴘ ɢʀᴀʙʙᴇʀꜱ
**━━━━━━━ᴄᴏᴍᴍᴀɴᴅꜱ━━━━━━━**
"""
        help_keyboard = [[InlineKeyboardButton("⤾ Back", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'back':
        caption = """
**🍃 ɢʀᴇᴇᴛɪɴɢꜱ, ɪ'ᴍ ˹ᴀɴɪᴍᴇ • ɢʀᴀʙʙᴇʀ ワイフ˼ 🫧, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!**

**━━━━━━━▧▣▧━━━━━━━**
⦾ ᴡʜᴀᴛ ɪ ᴅᴏ: ɪ sᴘᴀᴡɴ   
     ᴡᴀɪғᴜs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ғᴏʀ
     ᴜsᴇʀs ᴛᴏ ɢʀᴀʙ.
⦾ ᴛᴏ ᴜsᴇ ᴍᴇ: ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ
     ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀᴘ ᴛʜᴇ ʜᴇʟᴘ
     ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.
**━━━━━━━▧▣▧━━━━━━━**
"""

        keyboard = [
            [InlineKeyboardButton("✣  ᴀᴅᴅ ᴍᴇ  ✣", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("〄  ꜱᴜᴘᴘᴏʀᴛ  〄", url=f'https://t.me/{SUPPORT_CHAT}'), InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇꜱ ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("❖  ʜᴇʟᴘ  ❖", callback_data='help')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='Markdown')

# <======================================= HANDLERS ==================================================>
application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
application.add_handler(CallbackQueryHandler(button, pattern='help|back'))
help_handler = CommandHandler('help', help, block=False)
application.add_handler(help_handler)

# by https://github.com/lovetheticx
