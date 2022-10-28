import config
import telebot
import token
import random
import weather

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands= ['start'])


def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Random Number Generator')
    item3 = types.KeyboardButton('Узнать погоду в своём городе')
    item2 = types.KeyboardButton('Что делает этот бот?')


    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}! \n Я - {1.first_name}, бот, созданный от n1ghtrwl'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types= ['text'])


def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Random Number Generator':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Что делает этот бот?':
            bot.send_message(message.chat.id, 'Данный бот находится на стадии разработки и пока может только гененрировать числа, если есть какие то идеи - пишите @n1ghtrcrawler')
        elif message.text == 'Узнать погоду в своём городе':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Москва', callback_data='moscow')
            item2 = types.InlineKeyboardButton('Санкт-Петербург', callback_data='saint_petersburg')
            item3 = types.InlineKeyboardButton('Новосибирск', callback_data='novosibirsk')

            markup.add(item1,item2,item3)

            bot.send_message(message.chat.id, 'В каком городе ты живешь?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю, что ответить :(')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'moscow':
                bot.send_message(call.message.chat.id, weather.request_weather('Москва'))
                bot.send_message(call.message.chat.id, weather.request_weather_description('Москва'))
                bot.send_message(call.message.chat.id, weather.sun('Москва'))
            elif call.data == 'saint_petersburg':
                bot.send_message(call.message.chat.id, weather.request_weather('Санкт-Петербург'))
                bot.send_message(call.message.chat.id, weather.request_weather_description('Санкт-Петербург'))
                bot.send_message(call.message.chat.id, weather.sun('Санкт-Петербург'))
            elif call.data == 'novosibirsk':
                bot.send_message(call.message.chat.id, weather.request_weather("Новосибирск"))
                bot.send_message(call.message.chat.id, weather.request_weather_description("Новосибирск"))
                bot.send_message(call.message.chat.id, weather.sun("Новосибирск"))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='В каком городе ты живешь?', reply_markup=None)


            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='На этом пока всё))))))')
    except Exception as e:
        print(repr(e))
#RUN
bot.polling(none_stop=True)

