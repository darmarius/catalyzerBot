from telebot import types
from bot import bot

@bot.message_handler(commands=['start'])
def send1(message):
    # получаем объект пользователя
    user = message.from_user
    fullname = getFullName(user)
    # получаем username пользователя (если есть)
    welcome_message = f"""Привет, {fullname}!🙌

Ты тут! Это значит тебя интересует тема систематизации твоего бизнеса! 

Делегирования - это самый важный навык для руководителя, если он хочет выйти из операционки!

Поэтому дарю тебе чек-лист *"5 шагов к успешному делегированию задач"*!🥳

Он собран на основе многих успешных методологий построения задач и вобрал в себя только самое эффективное.

Круто? Конечно же)

Дальше больше, жми "Погнали", чтобы начать"""
    
    # отправляем приветственное сообщение с фотографией и кнопкой "Погнали"
    photo = open("assets/1.hi.jpg", 'rb')
    keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton(text="Погнали 🚀", callback_data="second")
    keyboard.add(start_button)
    bot.send_photo(message.chat.id, photo, caption=welcome_message, reply_markup=keyboard, parse_mode="Markdown")

def getFullName(user):
    fullname = ""
    try:
        first_name = user.first_name
        fullname += first_name + " "
    except:
        print(f"first_name is not accessable for @{user.username}")
        
    try:
        last_name = user.last_name
        fullname += last_name
    except:
            print(f"last_name is not accessable for @{user.username}")
    return fullname