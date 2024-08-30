import asyncio
import re
from pymongo import MongoClient
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from shivu import CHARA_CHANNEL_ID, application

# MongoDB connection
mongo_url = "mongodb+srv://yunyxedits:assalom%4013@waifudata.vfutysm.mongodb.net/?retryWrites=true&w=majority&appName=waifudata"
client = MongoClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters_lol']

# Global variable to control the upload process
uploading = False

def normalize_rarity(rarity):
    # Remove emojis and special characters for comparison
    return re.sub(r'[^\w\s]', '', rarity).strip().lower()

async def export_characters_to_channel(update: Update, context: CallbackContext):
    global uploading
    uploading = True  # Set the uploading flag to True

    # Get the rarity from the command arguments
    rarity_filter = context.args[0] if context.args else None

    # Normalize the rarity filter
    if rarity_filter:
        rarity_filter = normalize_rarity(rarity_filter)
        print(f"Filtering for rarity: {rarity_filter}")

    # Fetch all characters as a list
    characters = list(collection.find())
    total_uploaded = 0

    for character in characters:
        if not uploading:  # Check if uploading is still allowed
            await update.message.reply_text("Upload process stopped.")
            break

        normalized_rarity = normalize_rarity(character['rarity'])
        print(f"Checking character: {character['name']} with rarity: {character['rarity']} (normalized: {normalized_rarity})")

        # Filter by rarity if specified
        if rarity_filter and normalized_rarity != rarity_filter:
            continue

        img_url = character['img_url']
        name = character['name']
        anime = character['anime']
        rarity = character['rarity']
        character_id = character['id']

        # Prepare the caption for the message
        caption = f"<b>Character Name:</b> {name}\n<b>Anime Name:</b> {anime}\n<b>Rarity:</b> {rarity}\n<b>ID:</b> {character_id}"

        try:
            # Send the picture to the channel
            await context.bot.send_photo(
                chat_id=CHARA_CHANNEL_ID,
                photo=img_url,
                caption=caption,
                parse_mode='HTML'
            )
            total_uploaded += 1
            print(f"Uploaded character: {name} with ID: {character_id}")

            # Wait for 5 seconds before sending the next character
            await asyncio.sleep(5)

        except Exception as e:
            print(f"Failed to upload {name}: {str(e)}")

    if uploading:  # If still uploading, send final message
        await update.message.reply_text(f"Successfully uploaded {total_uploaded} characters to the channel.")
    uploading = False  # Reset the uploading flag

async def stop_uploading(update: Update, context: CallbackContext):
    global uploading
    uploading = False  # Set the uploading flag to False
    await update.message.reply_text("Upload process has been stopped.")

# Register the command handlers
EXPORT_HANDLER = CommandHandler('database', export_characters_to_channel)
STOP_HANDLER = CommandHandler('stopdata', stop_uploading)
application.add_handler(EXPORT_HANDLER)
application.add_handler(STOP_HANDLER)
