from telebot import telebot
from telebot import types
from tokens import tg_token



bot = telebot.TeleBot(tg_token)

print('start')

@bot.message_handler(commands=['start'])
def start(message):
    mti = message.chat.id
    bot.send_message(mti, 'hi Taras')



bot.polling(True)