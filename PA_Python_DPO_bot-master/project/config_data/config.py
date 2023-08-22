"""Конфиг для натсройки бота"""

from telebot import TeleBot
from telebot.storage import StateMemoryStorage

BOT_TOKEN ='6263501891:AAGnprgbLZW-WSkvT40wd9rcl-zPTIy3jMM'
RAPID_API_KEY = 'b66896be3dmsh3fe71d8032f8e78p119289jsne3b8359090a7'

storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)

BASE_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', 'Вывести самые дешевые отели в городе'),
    ('highprice', 'Вывести самые дорогие отели в городе'),
    ('bestdeal', 'Вывести отели, наиболее подходящие по цене и расположению от центра'),
    ('history', 'Вывести историю поиска отелей')
)

max_hotels_amount = 10
max_photos_amount = 5
USD = 80
