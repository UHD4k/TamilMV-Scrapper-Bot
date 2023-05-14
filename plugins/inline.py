from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)

@Client.on_inline_query()
async def inline(_, query: InlineQuery):
        string = query.query.lower()
        if string == "":
        	METHOD=  [ InlineQueryResultArticle( title="Enter Your Text", input_message_content=InputTextMessageContent("**Example :-** ```@Google_Translator_Star_Bot How are You # Tamil```"),description="{Text} # {language code}",thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        	await query.answer( results=METHOD,  cache_time=2, switch_pm_text="Using Method",switch_pm_parameter="start" )
        else:
        	splitit = string.split("#")        	     	
        try:
        		cd = splitit[1].lower().replace(" ", "")
        		text = splitit[0]
        except:
        	METHOD=  [ InlineQueryResultArticle( title="Enter Your Text", input_message_content=InputTextMessageContent("**Example :-** ```@Google_Translator_Star_Bot How are You # Tamil```"),description="{Text} # {language code} ",thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        	await query.answer( results=METHOD,  cache_time=2, switch_pm_text="Using Method",switch_pm_parameter="start" )
        	return
        try:
        	translator = Translator()
        	translation = translator.translate(text,dest = cd)
        except:
        	return
        TRTEXT=  [ InlineQueryResultArticle( title=f"Translated From {translation.src} To {translation.dest}", input_message_content=InputTextMessageContent(translation.text),description=f'{translation.text}',thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        try:
        	await query.answer(results=TRTEXT, reply_markup = get_reply_markup(query=string),  cache_time=2, switch_pm_text="Google Translater",switch_pm_parameter="start")
        except:
        	return

def get_reply_markup(query):
    buttons = [
        [
            InlineKeyboardButton('Translate Again', switch_inline_query_current_chat=query)
        ]
        ]
    return InlineKeyboardMarkup(buttons)
