"""
    Main file for bot woking
    Version: 1.0.0
    Author: Sequel
"""

from Configure.configure import TOKEN              # Импортируем TOKEN бота из файла конфигураций
from Translate.translate import Translate          # Импортируем класс-переводчик
import re                                          # Импорируем модуль регулярных выражений
import telebot as tbot                             # ИМпортруем библиотеку для создания Telegram бота

# Инициализируем телеграм бота через класс TeleBot, присваиваем в качестве аргумента token ботв
# из переменной TOKEN файла configure
bot = tbot.TeleBot(TOKEN)

# Создаем команду бота "/en" для перевода текса на английский
# (формат работы команды /en <текст для перевода на английский>)
@bot.message_handler(commands=['en'])
def en(message):
    # Фотрматируем текст сообщения убираем из него текст команды "/en"
    format_text_message = message.text.replace('/en', '', 1)

    # Отправляем текст переведенный текст в чат
    bot.send_message(
        message.chat.id,
        text=Translate(format_text_message).ru_en()
        )
# Все тоже самое только переводит на русский
@bot.message_handler(commands=['ru'])
def ru(message):

    format_text_message = message.text.replace('/ru', '', 1)

    bot.send_message(
        message.chat.id,
        text=Translate(format_text_message).en_ru()
        )

bot.polling(non_stop=True)