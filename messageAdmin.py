from telebot import types
from bot import bot
import db

def send(message):
    username = message.from_user.username
    if username == "intelligent12":
        # Получаем данные из таблицы users
        users = db.select_all_users()

        # Создаем заголовок таблицы
        table = "| Id | Username | Fullname | Chat ID | Phone | Register Date | Stage | File Sent|\n"
        table += "| -- | -------- | -------- | ------- | ----- | ------------- | ----- | --------- |"

        # Добавляем данные из таблицы в таблицу в формате Markdown
        for user in users:
            table += "\n"
            userid = user[0]
            username = user[1]
            fullname = user[2]
            chat_id = user[3]
            phone = user[4]
            register_date = user[5]
            stage = user[6]
            file_sent = user[7]
            userline = f"| {userid} | {username} | {fullname} | {chat_id} | {phone} | {register_date} | {stage} | {file_sent} |"
            userline = userline.replace("_","\_")
            userline = userline.replace("@","\@")
            userline = userline.replace("&","\&")
            table += userline
        print(table)
        # Отправляем сообщение с таблицей в формате Markdown
        bot.send_message(message.chat.id, table, parse_mode="Markdown")