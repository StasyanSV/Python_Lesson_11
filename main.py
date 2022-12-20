import telebot
from config import TOKEN
import encoding
import decoding

bot = telebot.TeleBot(TOKEN)

'''Команда START'''


@bot.message_handler(commands=['start'])
def welcome(message):
    '''КНОПКИ'''
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itemp1 = telebot.types.KeyboardButton('Кодирование текста')
    itemp2 = telebot.types.KeyboardButton('Декодирование текста')

    markup.add(itemp1, itemp2)  # добавили кнопку в множество

    # bot.send_message(message.chat.id, 'Добро пожаловать! Выбирите нужный Вам пункт меню: ', reply_markup=markup)
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name}! Что хочешь сделать?'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Кодирование текста':
        msg = bot.send_message(message.chat.id, f'Введите текст для кодировки:')
        bot.register_next_step_handler(msg, encoding.intxt)
    elif message.text == 'Декодирование текста':
        msg = bot.send_message(message.chat.id, f'Введите текст для кодировки:')
        bot.register_next_step_handler(msg, decoding.intxt)


bot.polling(none_stop=True)
