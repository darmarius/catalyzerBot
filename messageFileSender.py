from bot import bot
import db
import threading
import time

def send_file_later(chat_id):
    file_path = "files/5 шагов к успешному делегированию задач.pdf"
    def send_file():
        time.sleep(90)
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id, f, caption="Твой файл готов!")
            print(f"{chat_id} file sent")
    threading.Thread(target=send_file).start()
