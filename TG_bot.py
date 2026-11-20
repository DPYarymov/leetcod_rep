import telebot
# from telebot import types
import weatherByPoint

bot = telebot.TeleBot('7324627812:AAEEuwJWpK-CrNrbqZnDgzQLAWS2Ljar8xw')


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton('Прогноз погоды')
    button2 = telebot.types.KeyboardButton('Блэк Джэк')
    button3 = telebot.types.KeyboardButton('Шлюхи')

    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, 'Привет! Я бот Димана. Что Вас интересует?', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        if message.text == 'Прогноз погоды':
            bot.send_message(message.chat.id, 'В каком городе?')

            @bot.message_handler(func=lambda message: message.chat.id == message.chat.id)
            def handle_city_input(message):
                user_city = message.text
                temperature = str(weatherByPoint.weather_by_point(user_city))
                bot.send_message(message.chat.id, f'Температура воздуха в городе {user_city} {temperature}')

        elif message.text == 'Блэк Джэк':
            bot.reply_to(message, 'Диман эту кнопку не запрограммировал!')

        elif message.text == 'Шлюхи':
            bot.reply_to(message, 'Диман эту кнопку не запрограммировал!')

        else:
            bot.reply_to(message, 'Что Вас интересует?', reply_markup=keyboard)


# def asd(message):
#     global user_city
#     user_city = message.text
#     temperature = str(weatherByPoint.weather_by_point(user_city))
#     bot.send_message(message.chat.id, f'Температура воздуха в городе {user_city} {temperature}')

bot.polling()
