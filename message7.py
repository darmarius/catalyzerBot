from bot import bot
import db

def send(call):
    chat_id = call.data.replace("confirm","")
    my_confirm_message = """Сообщение увидел, скоро напишу!"""

    photo = open("assets/8.write.jpg", 'rb')
    bot.send_photo(chat_id, photo, caption=my_confirm_message, parse_mode="Markdown")
    db.update_stage(chat_id,7)