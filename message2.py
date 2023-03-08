from telebot import types
from bot import bot
import db
import messageFileSender

def send(call):
    # сохраняем информацию о пользователе в базу данных
    chat_id = call.message.chat.id
    handle_user(chat_id,call)
    messageFileSender.send_file_later(chat_id)

    # отправляем сообщение с файлом PDF и кнопкой "Да"
    presentation_message = """Чек-лист уже отправляется. Обычно на это надо 1-2 минуты)

А пока давай *кратко* расскажу о себе и продолжим.
Меня зовут Владислав Быковский - консультант по систематизации бизнеса.

Помогаю бизнесам с помощью: _
🔸Внедрения проектного управления
🔸Внедрение управленческих дашбордов и отчетности
🔸Аудит, оптимизация и автоматизация бизнес процессов
🔸Внедрение и настройка схемы организации
🔸Внедрение таск менеджера и базы знаний
🔸Настройка коммуникации_

✔️ В прошлом году закрыл 9 проектов на 25 000 000 ₽ и сэкономил клиентам 125 000 000 ₽!

✔️ Собрал лучшие практики ведения бизнес-процессов в крупных компаниях: Мегафон, СБЕР, ВТБ, Sony, НБ РБ и др.

✔️ Имею международную сертификацию

✔️ Вложил в своё образование > 2 000 000 ₽

Теперь давай вернёмся к тому, зачем ты здесь 👇"""

    photo = open("assets/2.me.jpg", 'rb')
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Давай продолжим", callback_data="third")
    keyboard.add(button)
    bot.send_photo(chat_id, photo, caption=presentation_message, reply_markup=keyboard, parse_mode="Markdown")

def handle_user(chat_id,call):
    username = call.from_user.username
    user = db.select_current_user(chat_id)
    if user:
        #пользователь уже есть в базе, просто обновляем дату
        db.update_current_user(chat_id)
        db.update_stage(chat_id,2)
    else:
        # получаем объект контакта пользователя (если есть)
        # если контакт есть, получаем номер телефона
        phone_number = ""
        try:
            if call.from_user.contact:
                phone_number = call.from_user.contact.phone_number
        except:
            print(f"Contact is not accessable for @{username}")

        fullname = ""
        try:
            first_name = call.from_user.first_name
            fullname += first_name + " "
        except:
            print(f"first_name is not accessable for @{username}")
        
        try:
            last_name = call.from_user.last_name
            fullname += last_name
        except:
            print(f"last_name is not accessable for @{username}")
        # Добавляем запись о пользователе в базу данных
        db.create_user(username, fullname, chat_id, phone_number)
    # сохраняем информацию в базу данных