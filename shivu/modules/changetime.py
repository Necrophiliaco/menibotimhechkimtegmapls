#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# For Waifu/Husbando telegram bots.
# Updated and Added new commands, features and style by https://github.com/lovetheticx
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# <============================================== IMPORTS =========================================================>

from pymongo import  ReturnDocument
from pyrogram.enums import ChatMemberStatus, ChatType
from shivu import user_totals_collection, shivuu
from pyrogram import Client, filters
from pyrogram.types import Message

ADMINS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

# <======================================= CHANGETIME FUNCTION ==================================================>

@shivuu.on_message(filters.command("changetime"))
async def change_time(client: Client, message: Message):
    
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await shivuu.get_chat_member(chat_id,user_id)
        

    if member.status not in ADMINS :
        await message.reply_text('⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n⛔️ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗗𝗠𝗜𝗡\n⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋ ')
        return

    try:
        args = message.command
        if len(args) != 2:
            await message.reply_text('⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n⚠️ Please write like this to change spawn time:\n/changetime 100 | 200 | 300. . .\n⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋')
            return

        new_frequency = int(args[1])
        if new_frequency < 100:
            await message.reply_text('⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n⚠️ 𝗧𝗛𝗘 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗥𝗘𝗤𝗨𝗘𝗡𝗖𝗬 𝗠𝗨𝗦𝗧 𝗕𝗘 𝗚𝗥𝗘𝗔𝗧𝗘𝗥 𝗧𝗛𝗔𝗡 𝗢𝗥 𝗘𝗤𝗨𝗔𝗟 𝗧𝗢 𝟭𝟬𝟬\n⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋ ')
            return

    
        chat_frequency = await user_totals_collection.find_one_and_update(
            {'chat_id': str(chat_id)},
            {'$set': {'message_frequency': new_frequency}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

        await message.reply_text(f'⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n❇️ 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗖𝗛𝗔𝗡𝗚𝗘𝗗! {new_frequency} 𝗡𝗢𝗪 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗚𝗘𝗧 𝗖𝗛𝗔𝗥𝗔𝗖𝗧𝗘𝗥 𝗘𝗩𝗘𝗥𝗬 𝟭𝟬𝟬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦!\n⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋')
    except Exception as e:
        await message.reply_text(f'⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n🛑 Failed to change {str(e)}⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋')

# <=============================================== END ==========================================================>
# by https://github.com/lovetheticx        