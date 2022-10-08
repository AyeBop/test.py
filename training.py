import telebot
from telebot import types
import test_pars

bot = telebot.TeleBot('5661855500:AAE9Vxss3Fyr4sZbgFxvX6-ruBznUML6i6Q')


@bot.message_handler(commands=['start'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    check_parse = types.KeyboardButton('🤪Место в списках')
    markup.add(check_parse)
    bot.send_message(message.chat.id, '12346', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def check_pos(message):
    if message.chat.type == 'private':
        if message.text == '🤪Место в списках':
            bot.send_message(message.chat.id, str(test_pars.your_position(test_pars.parse())))



bot.polling(none_stop=True)
