from telebot import telebot
from telebot import types
from tokens import tg_token
from func import download_telegram_photo
from detection import get_text
from sorting import formatting
from solving import gpt
import g4f as gf
import json
from data_func import create_user_data
from pprint import pprint as pp


bot = telebot.TeleBot(tg_token)

print('start')

@bot.message_handler(commands=['start'])
def start(message):

    create_user_data(message, 'user-data')

    
    bot.send_message(message.chat.id, message.from_user.language_code)



@bot.message_handler(content_types=['photo'])
def process_photo_task(message):
    mti = message.chat.id
    

    btns = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='with abc', callback_data='with')
    btn2 = types.InlineKeyboardButton(text='with out abc', callback_data='without',)
    
    btns.add(btn1, btn2)

    bot.send_message(message.chat.id, 'choose your type', reply_markup=btns)
    
    # bot.send_message(mti, 'your task processing...')
    
    # photo = download_telegram_photo(bot, message, 'photos/')
    
    # bot.send_message(mti, 'searching text')
    # text = get_text(photo)
    # print(text)
    
    # formated_text = formatting(text)
    # print(formated_text)
    
    # x = f'this is a test give me correct answere: \n{formated_text}'
    
    
    # bot.send_message(mti, 'solving')
    # solution = gpt(x, gf.models.gpt_35_turbo, None)
    
    # bot.send_message(mti, solution)
    
    

@bot.callback_query_handler(func=lambda call: True)
def checck_callback(call):
    try:
        # pp(call)
        bot.send_message(call.message.chat.id, call.message)

    except:
        pass
    
    
    
bot.polling(True)