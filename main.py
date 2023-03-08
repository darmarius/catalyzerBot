import message1
import message2
import message3
import message4
import message5
import message6
import message7
import message8
import messageAdmin
import os, sys
from bot import bot
from requests.exceptions import ConnectionError, ReadTimeout

@bot.message_handler(commands=['start'])
def send_welcome(message):
    message1.send(message)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "second":
        message2.send(call)
    elif call.data == "third":
        message3.send(call)
    elif call.data == "fourth":
        message4.send(call)
    elif call.data == "fifth":
        message5.send(call)
    elif  call.data== "done":
        message6.send(call)
    elif  call.data== "self":
        message6.self(call)
    elif  call.data.startswith("confirm"):
        message7.send(call)
    elif  call.data.startswith("failed"):
        message8.send(call)
    else:
        bot.answer_callback_query(call.id, text="Unknown action")
    

@bot.message_handler(func=lambda message: message.text.lower() == 'f')
def send_users_list(message):
    messageAdmin.send(message)

# запускаем бота
try:
    print("Бот работает!")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    print("Бот погиб но востал из пепла!")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
