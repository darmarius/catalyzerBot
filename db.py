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

def select_all_users():
    cursor.execute("SELECT * FROM users")
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