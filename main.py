import logging

import telebot
import os
from telebot import types
from flask import Flask, request

TOKEN = '5766023354:AAG5cbHs3fFtJFxO9VplTbXkqxMQm6xWRA0'
APP_URL = f'https://onlylabs.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    bot.send_message(id, 'Привет. Оно работает')


@server.route(f'/{TOKEN}', methods=['POST'])
def get_message():
    json_str = request.get_data().decode('utf-8')
    update = types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
