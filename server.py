import os

import telebot

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halooo, silakan upload filemu di sini")


@bot.message_handler(content_types=['document', 'audio', 'photo', 'video'])
def send_respon(message):
    bot.reply_to(message, "Yeayy, file berhasil terupload")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


print('BOT SUKSES BERJALAN!')

bot.infinity_polling()
