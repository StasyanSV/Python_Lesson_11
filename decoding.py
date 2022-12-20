import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def intxt(message):
    try:
        global user_num1

        user_num1 = str(message.text)
        # bot.send_message(message.chat.id, f'{decoding(user_num1)}') #Обычный ответ
        bot.reply_to(message, f'{decoding(user_num1)}') #Ответ с прикреплением сообщения
    except Exception as e:
        bot.reply_to(message, 'Что - то пошло не так')

    return user_num1

def decoding(user_num1):
    decoding = ''
    count = ''
    for char in user_num1:
        if char.isdigit():
            count += char
        elif int(count) == 0:
            decoding += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding #3A2B1D4C3R
