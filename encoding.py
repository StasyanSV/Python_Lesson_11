import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def intxt(message):
    try:
        global user_num1

        user_num1 = str(message.text)
        # print(user_num2)
        # bot.send_message(message.chat.id, f'{encoding(user_num1)}') #Обычный ответ
        bot.reply_to(message, f'{encoding(user_num1)}') #Ответ с прикреплением сообщения

    except:
        bot.reply_to(message, 'Что - то пошло не так')

    return user_num1

def encoding(user_num1):
    encoding = ''
    prev_char = ''
    count = 1

    for char in user_num1:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
    return encoding #AAABBDCCCCRRR