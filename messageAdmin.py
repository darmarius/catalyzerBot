from telebot import types
from bot import bot
import db

def send(message):
    admin_id = db.get_admin_user()[0][0]
    if admin_id == message.chat.id:
        admin_message = """Вот ваша админка, мой государь"""
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Список пользователей", callback_data=f"user_list")
        button2 = types.InlineKeyboardButton(text="Лист ожидания", callback_data=f"wait_list")
        button3 = types.InlineKeyboardButton(text="Статистика", callback_data=f"statistic")
        button4 = types.InlineKeyboardButton(text="Собрать дамп", callback_data=f"dump")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        send_to_admin(admin_message,keyboard)

def user_list():
    users = db.select_all_users()
    message = """Список всех пользователей к вашему вниманию:"""
    keyboard = users_keyboard(users)
    send_to_admin(message,keyboard)

def wait_list():
    users = db.select_all_users(" WHERE stage in (6,7,8)")
    message = """Список ожидающих пользователей к вашему вниманию:"""
    keyboard = users_keyboard(users)
    send_to_admin(message,keyboard)
    
def user_info(call):
    user_chat_id = call.data.replace("user_info","")
    user = db.select_current_user(user_chat_id)
    user_info_message = f"""Информация по пользователю @{user[0][1]}:
Fullname: {user[0][2]}
Chat ID: {user[0][3]}
Phone: {user[0][4]}
Register Date: {user[0][5]}
Stage: {user[0][6]}
File Sent: {user[0][7]}"""
    print(user_info_message)
    send_to_admin(user_info_message)

def statistic():
    users = db.get_statistic("users")
    stages = db.get_statistic("stage")
    message = f"Users count: {users[0][0]}\n"
    for stage in stages:
        message += f"Stage {stage[0]} - {stage[1]} users\n"
    send_to_admin(message)

def dump():
    table = ""
    users = db.select_all_users()
    for user in users:
        table += f"{user[0]};{user[1]};{user[2]};{user[3]};{user[4]};{user[5]};{user[6]};{user[7]}\n"
    print(table)
    send_to_admin(table)

def send_to_admin(message,keyboard=None):
    admin_id = db.get_admin_user()[0][0]
    bot.send_message(admin_id, message, reply_markup=keyboard)

def users_keyboard(users):
    keyboard = types.InlineKeyboardMarkup()
    for user in users:
        button = types.InlineKeyboardButton(text=f"{user[2]} - @{user[1]}", callback_data=f"user_info{user[3]}")
        keyboard.add(button)
        print(f"{user[0]}. @{user[1]} added to list")
    return keyboard

def import_users(message):
    admin_id = db.get_admin_user()[0][0]
    if admin_id == message.chat.id:
        user_data = []
        for user_line in message.text.splitlines()[1:]:
            user_values = user_line.split(";")
            user_data.append((
                int(user_values[0].strip()), # id
                user_values[1].strip(),     # username
                user_values[2].strip(),     # fullname
                int(user_values[3].strip()), # chat_id
                user_values[4].strip(),     # phone
                user_values[5].strip(),     # register_date
                int(user_values[6].strip()), # stage
                None if user_values[7].strip() == "None" else bool(user_values[7].strip()) # file_sent
            ))
        db.import_users(user_data)