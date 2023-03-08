from telebot import types
from bot import bot
import db

def send(call):
    chat_id = call.message.chat.id
    confirm_message = """Сообщение уже отправлено мне, скоро постучусь в личку.
    
Проверь, пожалуйста, что в настройках приватности к тебе можно достучаться!"""
    
    photo = open("assets/6.sent.jpg", 'rb')
    bot.send_photo(chat_id, photo, caption=confirm_message, parse_mode="Markdown")
    db.update_stage(chat_id,6)

    admin_message = "Он изволил просить вашей милости, чтобы вы ему отправили письмо."
    send_message_to_admin(chat_id,admin_message)

def self(call):
    chat_id = call.message.chat.id
    confirm_message = """Принято! 
Жду твоего сообщения."""

    photo = open("assets/7.wait.jpg", 'rb')
    bot.send_photo(chat_id, photo, caption=confirm_message, parse_mode="Markdown")
    db.update_stage(chat_id,6)

    admin_message = "Он понимает вашу загрузку и готов написать вам самостоятельно. Какой молодец!"
    send_message_to_admin(chat_id,admin_message)





def send_message_to_admin(chat_id,action):
    admin = db.get_admin_user()
    admin_id = admin[0][0]

    user = db.select_current_user(chat_id)
    username = user[0][1]
    username = username.replace("_","\_")
    username = username.replace("@","\@")
    username = username.replace("&","\&")

    confirm_message = f"""Милостивый государь,
У нас новый клиент @{username}!
{action}."""
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Ща напишу", callback_data=f"confirm{chat_id}")
    button2 = types.InlineKeyboardButton(text="Не могу написать", callback_data=f"failed{chat_id}")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(admin_id, confirm_message, reply_markup=keyboard, parse_mode="Markdown")