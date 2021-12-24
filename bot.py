import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/Hi.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton("/help")
    i2 = types.KeyboardButton("💃")
    i3 = types.KeyboardButton("😭")
    i4 = types.KeyboardButton("😃")
    i5 = types.KeyboardButton("🔞")
    i6 = types.KeyboardButton("🎵")
    i7 = types.KeyboardButton("👍")
    markup.add(i1, i2, i3, i4, i5, i6, i7)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nБот: {1.first_name}".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def ans(message):
    if message.chat.type == 'private':
        if message.text == '💃':
            sti = open('static/dance.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            sti = open('static/dance1.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            sti = open('static/dance2.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            sti = open('static/dance3.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text == '/help':
            bot.send_message(message.chat.id, 'Ботик присылает анимированные стикеры по эмодзи)')
            bot.send_message(message.chat.id, 'На команду "как дела?" бот пришлет новости')
            bot.send_message(message.chat.id, 'На команду "число" бот пришлет рандомное число')
        elif message.text == "😭":
            sti = open('static/cry.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text == "😃":
            sti = open('static/smile.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text == "🔞":
            sti = open('static/18.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text == "🎵":
            sti = open('static/music.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            sti = open('static/music1.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text == "👍":
            sti = open('static/ok.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            sti = open('static/ok1.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif message.text.lower() == "как дела?":
            bot.send_message(message.chat.id, 'Вот такие дела - https://ria.ru/')
        elif message.text.lower() == "число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        else:
            sti = open('static/error.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Ботик тебя не понимает(')


bot.polling(none_stop=True)
