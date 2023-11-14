from telebot import telebot
from telebot import types
from tokens import tg_token
from func import download_telegram_photo
from detection import get_text
from sorting import formatting
from solving import gpt
import g4f as gf


bot = telebot.TeleBot(tg_token)

print('start')

@bot.message_handler(commands=['start'])
def start(message):
    mti = message.chat.id
    bot.send_message(mti, 'hi Taras')



@bot.message_handler(content_types=['photo'])
def process_photo_task(message):
    mti = message.chat.id
    bot.send_message(mti, 'your task processing...')
    
    photo = download_telegram_photo(bot, message, 'photos/')
    
    bot.send_message(mti, 'searching text')
    text = get_text(photo)
    print(text)
    
    formated_text = formatting(text)
    print(formated_text)
    
    x = f'this is a test give me correct answere: \n{formated_text}'
    
    
    bot.send_message(mti, 'solving')
    solution = gpt(x, gf.models.gpt_35_turbo, None)
    
    bot.send_message(mti, solution)
    
    

bot.polling(True)