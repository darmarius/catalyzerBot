from telebot import types
from bot import bot
import db

def send(call):
    chat_id = call.message.chat.id
    pain_message = """*Твоя ситуация сейчас:* 

🔹 Команда работает в пол силы 😴

🔹 Сотрудники _"тупят"_ над задачами и результат не совпадает с ожиданиями 🤔

🔹 Исполнение сроков не является сильной стороной компании 😒

🔹 Нет контроля над работой сотрудников 😞

🔹 Сотрудники не понимают за что отвечают и какие у них KPI 😦

🔹 Хочется наконец-то *ОТДОХНУТЬ* от постоянного напряжения 🏖🏝

Есть такое?"""

    photo = open("assets/3.you.jpg", 'rb')
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Да, есть😢", callback_data="fourth")
    keyboard.add(button)
    bot.send_photo(chat_id, photo, caption=pain_message, reply_markup=keyboard, parse_mode="Markdown")
    db.update_stage(chat_id,3)