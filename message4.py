from telebot import types
from bot import bot
import db

def send(call):
    chat_id = call.message.chat.id
    pain_message = """А хочется: 

🔹 Автономный бизнес, который сам зарабатывает деньги.💸

🔹 Думать как развивать компанию, а не решать операционные вопросы.📈

🔹 Задачи выполняются чётко и в срок.✅

🔹 Сократить затраты на автоматизации рутины.💵

🔹 100% ясносная картина ситуации в бизнесе.🧐

🔹 Больше времени на семью и хобби.👨‍👩‍👦‍👦

Согласны со мной?"""

    photo = open("assets/4.want.jpg", 'rb')
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="ДА❗️", callback_data="fifth")
    keyboard.add(button)
    bot.send_photo(chat_id, photo, caption=pain_message, reply_markup=keyboard, parse_mode="Markdown")
    db.update_stage(chat_id,4)