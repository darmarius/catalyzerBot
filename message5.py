from telebot import types
from bot import bot
import db

def send(call):
    chat_id = call.message.chat.id
    last_message = """Ты красавчик раз дошел до сюда - ты уже готов что-то менять!
    
Приглашаю тебя на *бесплатную* консультацию! Это классная возможность обсудить все детали и ничего не упустить)

*На консультации мы обязательно:*

1. Разберём твой бизнес по полочкам

2. Найдём якоря, которые тянут бизнес вниз 

3. Обсудим, какие инструменты нужно внедрить прямо сейчас
    
Так же расскажу о своей методологии, как оптимизировать бизнес-процессы компании, чтобы расправиться с операционкой и двигаться вперёд! 
    
Кликай "Записаться🔥" и я свяжусь с тобой в течении часа, выберем и назначим удобное для тебя время консультации."""

    photo = open("assets/5.coolman.jpg", 'rb')
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Записаться🔥", callback_data="done")
    keyboard.add(button)
    bot.send_photo(chat_id, photo, caption=last_message, reply_markup=keyboard, parse_mode="Markdown")
    db.update_stage(chat_id,5)