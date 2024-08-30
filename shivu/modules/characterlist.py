#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# For Waifu/Husbando telegram bots.
# Updated and Added new commands, features and style by https://github.com/lovetheticx
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# <============================================== IMPORTS =========================================================>

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import CommandHandler, CallbackQueryHandler, InlineQueryHandler, CallbackContext
from shivu import application, collection

# <====================================== CHRACTER LIST FUNCTION ==================================================>

async def chlist(update: Update, context: CallbackContext):
    await display_character_list(update, context, 0)

async def display_character_list(update: Update, context: CallbackContext, page: int):
    all_characters = await collection.find({}).to_list(length=None)
    grouped_characters = {}
    for character in all_characters:
        if character['anime'] not in grouped_characters:
            grouped_characters[character['anime']] = []
        grouped_characters[character['anime']].append(character)

    total_pages = len(grouped_characters) // 10 + (len(grouped_characters) % 10 > 0)

    if page < 0 or page >= total_pages:
        page = 0

    keyboard = []
    for i, anime in enumerate(list(grouped_characters.keys())[page * 10:(page + 1) * 10]):
        keyboard.append([InlineKeyboardButton(f"{anime} ({len(grouped_characters[anime])})", callback_data=f"chlist:{page}:{i}")])

    keyboard.append([InlineKeyboardButton("🔍 Search", switch_inline_query_current_chat="")])

    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton("⬅️", callback_data=f"chlist:{page - 1}:0"))
    if page < total_pages - 1:
        navigation_buttons.append(InlineKeyboardButton("➡️", callback_data=f"chlist:{page + 1}:0"))
    if navigation_buttons:
        keyboard.append(navigation_buttons)

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("Select an anime to view its characters:", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text("Select an anime to view its characters:", reply_markup=reply_markup)

# <============================================== CALLBACK =========================================================>
        
async def character_list_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data.split(":")
    page = int(data[1])
    index = int(data[2])

    if index == 0:
        await display_character_list(update, context, page)
        return

    all_characters = await collection.find({}).to_list(length=None)
    grouped_characters = {}
    for character in all_characters:
        if character['anime'] not in grouped_characters:
            grouped_characters[character['anime']] = []
        grouped_characters[character['anime']].append(character)

    anime = list(grouped_characters.keys())[page * 10 + index]
    characters = sorted(grouped_characters[anime], key=lambda x: x['rarity'], reverse=True)

    message = f"<b>{anime}</b>\n\n"
    for character in characters:
        message += f"{character['id']} {character['name']} ({character['rarity']})\n"

    keyboard = [
        [InlineKeyboardButton("🔙 Back", callback_data=f"chlist:{page}:0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(message, parse_mode="HTML", reply_markup=reply_markup)

# <=========================================== INLINE SEARCH =======================================================>
async def inline_search(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if query:
        all_characters = await collection.find({}).to_list(length=None)
        matching_characters = [char for char in all_characters if query.lower() in char['name'].lower()]
        matching_characters = sorted(matching_characters, key=lambda x: x['rarity'], reverse=True)

        results = [
            InlineQueryResultArticle(
                id=char['id'],
                title=f"{char['name']} ({char['rarity']})",
                input_message_content=InputTextMessageContent(
                    f"{char['id']} {char['name']} ({char['rarity']})"
                )
            )
            for char in matching_characters[:50]
        ]

        await update.inline_query.answer(results)

# <======================================= HANDLERS ==================================================>
application.add_handler(CommandHandler("chlist", chlist, block=False))
application.add_handler(CallbackQueryHandler(character_list_callback, pattern="^chlist", block=False))
application.add_handler(InlineQueryHandler(inline_search, block=False))
# <========================================= END =====================================================>
# by https://github.com/lovetheticx