import telebot
from telebot import custom_filters
from telebot import types

token = 'token'
bot = telebot.TeleBot(token, parse_mode = None)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('PISB')
itembtn2 = types.KeyboardButton('PASC')
itembtn3 = types.KeyboardButton('PCSB')

itembtna = types.KeyboardButton('NSS')
itembtnv = types.KeyboardButton('Robotics')
itembtnc = types.KeyboardButton('GDU')
itembtnd = types.KeyboardButton('DEBSOC')
itembtne = types.KeyboardButton('PNAB')
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
