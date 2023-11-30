import os
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from helper.database import insert

FORCE_SUB = os.environ.get("FORCE_SUB", "Star_Bots_Tamil") 

async def not_subscribed(_, client, message):
    await insert(int(message.chat.id))
    if not FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    mention = message.from_user.mention
    buttons = [[InlineKeyboardButton(text="📢 Join Update Channel", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**Hello {mention} 💗,\nJoin Our Bot Updates Channel To Use Me ☺️\nYou Need to Join Our Channel to Use me\nKindly Please Join Our Channel**"
    try:
        user = await client.get_chat_member(FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="**Sorry You're Banned to Use Me**")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          
