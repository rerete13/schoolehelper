from telebot import telebot
from telebot import types
from tokens import tg_token
from func import download_telegram_photo
from detection import get_text
from sorting import formatting
from solving import gpt
import g4f as gf
import json
from data_func import create_user_data, add_user_data
from pprint import pprint as pp
from bot_func import wikamp_task_comliter, download_photo_by_file_id
import datetime

bot = telebot.TeleBot(tg_token)

print('start')

@bot.message_handler(commands=['start'])
def start(message):

    create_user_data(message, 'user-data')

    
    bot.send_message(message.chat.id, message.from_user.language_code)

    # with open(f"user-data/{message.chat.id}.json", "r") as f:
    #     data = json.load(f)
        
    # bot.send_photo(message.chat.id, data['photo-path'][-1][1])



@bot.message_handler(content_types=['photo'])
def process_photo_task(message):

    file_id = message.photo[-1].file_id
    
    add_user_data(f'user-data/{message.chat.id}', 'photo-path', file_id, data_update_path_in=None)
    


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
        
        if call.data == 'with':
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, 'wait untill bot process your task...')
            
            with open(f"user-data/{call.message.chat.id}.json", "r") as f:
                data = json.load(f)

            download_photo_by_file_id(bot, call.message, data['photo-path'][-1][1], 'photos', name=None)
            
            

    except:
        pass
    
    
    
bot.polling(True)