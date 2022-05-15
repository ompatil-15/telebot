import telebot
from telebot import custom_filters
from telebot import types

token = 'token'
bot = telebot.TeleBot(token, parse_mode = None)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('Chemistry')
itembtn2 = types.KeyboardButton('Physics')
itembtn3 = types.KeyboardButton('EM 1')

itembtna = types.KeyboardButton('EM 2')
itembtnv = types.KeyboardButton('PPS')
itembtnc = types.KeyboardButton('BXE')
itembtnd = types.KeyboardButton('ES')
itembtne = types.KeyboardButton('EG')
markup.add(itembtn1, itembtn2, itembtn3,itembtna,itembtnv,itembtnc,itembtnd,itembtne)
bot.send_message(5011331204, "SUBJECTS", reply_markup=markup)

@bot.message_handler(text = ['Em','Chemistry'])
def echo_all(message):
    chat_id = message.from_user.id
    bot.reply_to(message, 'INITIATED')
    doc = open('images.png','rb')
    bot.send_photo(chat_id,doc)
    print(chat_id)

@bot.message_handler(func = lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
