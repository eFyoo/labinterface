import sqlite3
import telebot
from telebot import types
import json

conn=sqlite3.connect("C:/SQLtelegram/telegram.db", check_same_thread=False)
cur = conn.cursor()


webAppT = types.WebAppInfo("https://efyoo.github.io/labinterface/")
token='7017525011:AAF3hhyYp6ivi5SJyAwbWfyZT_Gc9V2oWX4'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def menu(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 key_visitka = types.KeyboardButton("О нас")
 key_aboutdogs = types.KeyboardButton("Информация о собаках")
 key_map = types.KeyboardButton("Показать магазин на карте")
 key_knopka = types.KeyboardButton("Посмотреть собак", web_app=webAppT)
 keyboard.add(key_visitka, key_aboutdogs)
 keyboard.add(key_map, key_knopka)
 bot.send_message(message.chat.id, text = 'Привет, добро пожаловать в основное меню ✌️', reply_markup=keyboard)


@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
   data = json.loads(webAppMes.web_app_data.data)
   print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
   bot.send_message(webAppMes.chat.id, "Кнопка отреагировала на клик:")
   bot.send_message(webAppMes.chat.id, data)
   bot.send_sticker(webAppMes.chat.id, sticker = "CAACAgEAAxkBAAEuTtdnBwUE1NzPbKcEbp_Zdn1mhqQ8FwAC-AEAAjgOghFb9OZ62rUyZDYE")
   

@bot.message_handler(content_types = ['text'])
def callback_worker(message):
 if message.text == "О нас":
  bot.send_message(message.chat.id, "Огромный выбор товаров для животных на сайте зоомагазина Четыре лапы и хвост. Акции и бесплатная доставка на дом по Самаре. Заказывайте недорого!")
  bot.send_sticker(message.chat.id, sticker = "CAACAgEAAxkBAAEuPx9nBF9O7Ggv70Ohp2HGL0CnSTzBwAACVgcAAuTKcwqguVpucUDEoTYE")
  
 elif message.text == "Показать магазин на карте":
  bot.send_message(message.chat.id, 'Мы находимся по адресу: г.Самара, Галактиновская 171. Вот наше местоположение на карте:')
  bot.send_location(message.from_user.id, 53.1998, 50.1077)
  bot.send_sticker(message.chat.id, sticker = "CAACAgIAAxkBAAEuPytnBGEmDJ9IQuxheIbbRIlHFjenhAACMgoAAm4y2AAB_W-265DwO002BA") 

 elif message.text == "Информация о собаках":
  dogs_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
  dogs_menu.add('Мопс', 'Бернедудль')
  dogs_menu.add('Бассет-хаунд', 'Аффенпинчер')
  dogs_menu.add('Назад')
  bot.send_message(message.chat.id, 'Выберите собаку', reply_markup=dogs_menu)

 elif message.text == "Мопс":
   mopsName = conn.execute('Select dogname from Dogs WHERE id == 15').fetchone()
   mopsDesc = conn.execute('Select desc from Dogs WHERE id == 15').fetchone()
   mopsAge = conn.execute('Select age from Dogs WHERE id == 15').fetchone()
   mopsImage = open("./mops.jpg", 'rb')
   bot.send_message(message.chat.id, mopsName)
   bot.send_message(message.chat.id, mopsDesc)
   bot.send_message(message.chat.id, mopsAge)
   bot.send_photo(message.chat.id, mopsImage)

 elif message.text == "Бернедудль":
   bernName = conn.execute('Select dogname from Dogs WHERE id == 14').fetchone()
   bernDesc = conn.execute('Select desc from Dogs WHERE id == 14').fetchone()
   bernAge = conn.execute('Select age from Dogs WHERE id == 14').fetchone()
   bernImage = open("./Bernedoodle1.jpg", 'rb')
   bot.send_message(message.chat.id, bernName)
   bot.send_message(message.chat.id, bernDesc)
   bot.send_message(message.chat.id, bernAge)
   bot.send_photo(message.chat.id, bernImage)

 elif message.text == "Бассет-хаунд":
   bassName = conn.execute('Select dogname from Dogs WHERE id == 11').fetchone()
   bassDesc = conn.execute('Select desc from Dogs WHERE id == 11').fetchone()
   bassAge = conn.execute('Select age from Dogs WHERE id == 11').fetchone()
   bassImage = open("./bass.jpg", 'rb')
   bot.send_message(message.chat.id, bassName)
   bot.send_message(message.chat.id, bassDesc)
   bot.send_message(message.chat.id, bassAge)
   bot.send_photo(message.chat.id, bassImage)

 elif message.text == "Аффенпинчер":
   affName = conn.execute('Select dogname from Dogs WHERE id == 10').fetchone()
   affDesc = conn.execute('Select desc from Dogs WHERE id == 10').fetchone()
   affAge = conn.execute('Select age from Dogs WHERE id == 10').fetchone()
   affImage = open("./aff.jpg", 'rb')
   bot.send_message(message.chat.id, affName)
   bot.send_message(message.chat.id, affDesc)
   bot.send_message(message.chat.id, affAge)
   bot.send_photo(message.chat.id, affImage)

 elif message.text == "Назад":
   menu(message)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()

