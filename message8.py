from telebot import types
from bot import bot
import db

def send(call):
    chat_id = call.data.replace("failed","")
    failed_response__message = """Не могу до тебя достучаться! 
Проверь пожалуйста настройки или напиши мне сам @intelligent12"""

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Сейчас сам напишу", callback_data=f"self")
    button2 = types.InlineKeyboardButton(text="Поправил настройки, попробуй еще раз", callback_data=f"done")
    keyboard.add(button1)
    keyboard.add(button2)
    photo = open("assets/9.cantwrite.jpg", 'rb')
    bot.send_photo(chat_id, photo, caption=failed_response__message, reply_markup=keyboard, parse_mode="Markdown")
    db.update_stage(chat_id,8)