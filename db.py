import sqlite3
from datetime import datetime

# Создаем базу данных и таблицу
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT,
                  fullname TEXT,
                  chat_id INTEGER, 
                  phone TEXT, 
                  register_date DATE,
                  stage INTEGER,
                  file_sent BOOLEAN)""")
conn.commit()

def select_current_user(chat_id):
    cursor.execute(f"SELECT * FROM users WHERE chat_id = {chat_id}")
    user = cursor.fetchall()
    return user

def update_current_user(chat_id):
    register_date = datetime.now().strftime('%Y-%m-%d')  # текущая дата
    cursor.execute("UPDATE users SET register_date = ? WHERE chat_id = ?", (register_date, chat_id))
    conn.commit()
    print(f"{chat_id} register_date updated")

def create_user(username, fullname, chat_id, phone_number):
    register_date = datetime.now().strftime('%Y-%m-%d')  # текущая дата
    cursor.execute("INSERT INTO users (username, fullname, chat_id, phone, register_date,stage) VALUES (?, ?, ?, ?, ?, ?)",
                    (username, fullname, chat_id, phone_number, register_date,2))
    conn.commit()
    print(f"{username} added to database")

def select_all_users(condition=None):
    query = "SELECT * FROM users"
    if condition!=None:
        query += condition
    print(query)
    cursor.execute(query)
    users = cursor.fetchall()
    return users

def update_stage(chat_id,stage):
    cursor.execute("UPDATE users SET stage = ? WHERE chat_id = ?", (stage, chat_id))
    conn.commit()
    print(f"{chat_id} stage updated to {stage}")

def update_file_sent(chat_id):
    cursor.execute("UPDATE users SET file_sent = 1 WHERE chat_id = ?", (chat_id))
    conn.commit()
    print(f"{chat_id} file_sent")

def get_admin_user():
    cursor.execute("SELECT chat_id FROM users WHERE username = 'intelligent12'")
    user = cursor.fetchall()
    return user

def get_statistic(mode):
    query = "SELECT COUNT(*) FROM users"
    if mode == "stage":
        query = "SELECT stage,COUNT(*) FROM users GROUP BY stage"
    cursor.execute(query)
    statistic = cursor.fetchall()
    return statistic

def import_users(user_data):
    for user in user_data:
        # Ищем пользователя по его ID
        cursor.execute("SELECT * FROM users WHERE id=?", (user[0],))
        existing_user = cursor.fetchone()
        # Если пользователь уже есть в базе данных, обновляем его запись
        if existing_user:
            cursor.execute("UPDATE users SET username=?, fullname=?, phone=?, register_date=?, stage=?, file_sent=? WHERE chat_id=?",
                      (user[1], user[2], user[4], user[5], user[6], user[7], user[3]))
            print(f"User @{user[1]} - {user[3]} updated")
        # Иначе создаем новую запись в таблице
        else:
            cursor.execute("INSERT INTO users (username, fullname, chat_id, phone, register_date, stage, file_sent) VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (user[1], user[2], user[3], user[4], user[5], user[6], user[7]))
            print(f"User @{user[1]} - {user[3]} added")
    # Сохраняем изменения в базе данных
    conn.commit()