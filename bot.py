import os
import telebot

TOKEN = os.getenv('BOT_API_KEY')
bot = telebot.TeleBot(TOKEN)