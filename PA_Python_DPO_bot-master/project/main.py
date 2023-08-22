"""
Основной файл для запуска бота. (python main.py)
содержит ьвсе доступные handlers
"""

import os
from datetime import date, datetime, timedelta
from typing import List, Dict, Optional

from telebot.custom_filters import StateFilter
from loguru import logger
from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery
from telegram_bot_calendar import DetailedTelegramCalendar

from commands.find_city import find_city
from commands.find_hotel import find_lowprice, find_highprice, find_bestdeal
from commands.hotel_detail import hotel_details
from commands.result_output import result_output, hotels_searches_output
from config_data.config import bot, BASE_COMMANDS

from commands.set_base_commands import set_base_commands
from database.database import create_tables, write_data, hotels_history_from_db, HotelsSearch, hotels_data_from_db, \
    days_in_hotels_from_db
from keyboards.calendar_ru import LSTEP
from keyboards.inline.cities import city_markup
from keyboards.inline.hotels import hotels_markup
from keyboards.inline.photos import photos_markup
from logs.loggers import func_logger
from states.history import get_hotels_search
from states.search_info import SearchInfoState

if __name__ == '__main__':
    logger.add(os.path.join('logs', 'logs.log'),
               format='{time} {level} {message}',
               retention='2 days')
    logger.debug('=== Новый запуск ===')

    create_tables()

    bot.add_custom_filter(StateFilter(bot))

    set_base_commands(bot)


    @bot.message_handler(commands=['start'])
    @func_logger
    def bot_start(message: Message):
        bot.reply_to(message, f"Привет, {message.from_user.full_name}!")


    @bot.message_handler(commands=['help'])
    @func_logger
    def bot_help(message: Message):
        text = [f'/{command} - {desk}' for command, desk in BASE_COMMANDS]
        bot.reply_to(message, '\n'.join(text))


    """handlers for search commands"""

    @bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
    @func_logger
    def start_search(message: Message) -> None:
        """
         Начало поиска отелей:
        - запрашивается город для поиска
        - сохраняется информация о пользователе и введенной команде

        params:
        :message: сообщение
        """
        logger.info(f'Начало поиска (команда: {message.text})')
        user_id: int = message.from_user.id
        chat_id: int = message.chat.id
        logger.info(f'user_id = {user_id}; chat_id = {chat_id}')

        bot.set_state(user_id, SearchInfoState.city, chat_id)
        bot.send_message(user_id, 'В каком городе искать отель?')

        with bot.retrieve_data(user_id, chat_id) as data:
            data['command'] = message.text
            data['date_time'] = datetime.utcnow().strftime('%d.%m.%Y %H:%M:%S')
            data['user_id'] = user_id
            data['chat_id'] = chat_id
            data['user_name'] = message.from_user.full_name


    @bot.message_handler(state=SearchInfoState.city)
    @func_logger
    def city_for_search(message: Message) -> None:
        """
        уточняется город для поиска

        params:
        :message: сообщение
        """

        user_id: int = message.from_user.id
        chat_id: int = message.chat.id

        cities_dict: Dict[str, str] = find_city(message.text)
        if cities_dict:
            with bot.retrieve_data(user_id, chat_id) as data:
                data['cities'] = cities_dict
            cities_keyboard: InlineKeyboardMarkup = city_markup(cities_dict)
            text: str = 'Уточните место поиска:'
            bot.send_message(user_id, text, reply_markup=cities_keyboard)
            bot.set_state(user_id, SearchInfoState.get_city, chat_id)
        else:
            text: str = 'Похоже произошла ошибка! ' \
                        '\nПопробуйте еще раз.' \
                        '\nВ каком городе будем искать?'
            bot.send_message(user_id, text)


    @bot.callback_query_handler(func=None, state=SearchInfoState.get_city)
    @func_logger
    def get_city(call: CallbackQuery) -> None:
        """
        сохраняется город для поиска
        запрашивается дата заезда в отель

        params:
        :call: callback
        """

        user_id: int = call.from_user.id
        chat_id: int = call.message.chat.id
        message_id: int = call.message.message_id

        with bot.retrieve_data(user_id, chat_id) as data:
            city_id: str = call.data
            data['city_id'] = city_id
            data['city'] = data['cities'][city_id]
            del data['cities']
            city: str = data['city']
        text: str = f'Место для поиска: {city}'
        bot.edit_message_text(text, chat_id, message_id)
        logger.info(text)

        calendar, step = DetailedTelegramCalendar(calendar_id=1, locale='ru',
                                                  min_date=date.today()
                                                  ).build()

        bot.send_message(user_id, f'Укажите дату заезда: выберите {LSTEP[step]}',
                         reply_markup=calendar)
        bot.set_state(user_id, SearchInfoState.date_in, chat_id)


    @bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1),
                                state=SearchInfoState.date_in)
    @func_logger
    def get_date_in(call: CallbackQuery) -> None:
        """
        сохраняется дата заезда в отель
        запрашивается дата отъезда

        params:
        :call: callback
        """

        user_id: int = call.from_user.id
        chat_id: int = call.message.chat.id
        message_id: int = call.message.message_id

        result, key, step = DetailedTelegramCalendar(calendar_id=1,
                                                     locale='ru',
                                                     min_date=date.today()
                                                     ).process(call.data)
        if not result and key:
            bot.edit_message_text(f"Укажите дату заезда: выберите {LSTEP[step]}",
                                  chat_id, message_id, reply_markup=key)
        elif result:
            text: str = f"Дата заезда: {result.strftime('%d.%m.%Y')}"
            bot.edit_message_text(text, chat_id, message_id)
            logger.info(text)
            with bot.retrieve_data(user_id, chat_id) as data:
                data['date_in'] = result.strftime('%d.%m.%Y')
                min_date: date = result + timedelta(days=1)

            calendar, step = DetailedTelegramCalendar(calendar_id=2, locale='ru',
                                                      min_date=min_date
                                                      ).build()
            bot.set_state(user_id, SearchInfoState.date_out, chat_id)
            bot.send_message(user_id, 'Укажите дату выезда: '
                                      f'выберите {LSTEP[step]}',
                             reply_markup=calendar)


    @bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2),
                                state=SearchInfoState.date_out)
    @func_logger
    def get_date_out(call: CallbackQuery) -> None:
        """
        сохраняется дата выезда из отеля
        запрашивается количество отелей

        params:
        :call: callback
        """

        user_id: int = call.from_user.id
        chat_id: int = call.message.chat.id
        message_id: int = call.message.message_id

        with bot.retrieve_data(user_id, chat_id) as data:
            min_date: date = (datetime.strptime(data['date_in'], '%d.%m.%Y') +
                              timedelta(days=1)).date()
        result, key, step = DetailedTelegramCalendar(calendar_id=2,
                                                     locale='ru',
                                                     min_date=min_date
                                                     ).process(call.data)
        if not result and key:
            bot.edit_message_text(f"Укажите дату выезда: выберите {LSTEP[step]}",
                                  chat_id, message_id, reply_markup=key)
        elif result:
            text: str = f"Дата выезда: {result.strftime('%d.%m.%Y')}"
            bot.edit_message_text(text, chat_id, message_id)
            logger.info(text)

            with bot.retrieve_data(user_id, chat_id) as data:
                data['date_out'] = result.strftime('%d.%m.%Y')
            bot.set_state(user_id, SearchInfoState.hotels_amount, chat_id)
            bot.send_message(user_id, 'Какое количество отелей вывести?',
                             reply_markup=hotels_markup())


    @bot.callback_query_handler(func=None, state=SearchInfoState.hotels_amount)
    @func_logger
    def get_hotels_amount(call: CallbackQuery) -> None:
        """
        сохраняется количество отелей
        запрашивается количество фотографий для вывода

        params:
        :call: callback
        """

        user_id: int = call.from_user.id
        chat_id: int = call.message.chat.id
        message_id: int = call.message.message_id

        text: str = f'Количество отелей для вывода: {call.data}'
        bot.edit_message_text(text, chat_id, message_id)
        logger.info(text)
        bot.set_state(user_id, SearchInfoState.photos, chat_id)
        text: str = 'Сколько фотографий выводить для каждого отеля?'
        bot.send_message(user_id, text, reply_markup=photos_markup())
        with bot.retrieve_data(user_id, chat_id) as data:
            data['hotels_amount'] = int(call.data)


    @bot.callback_query_handler(func=None, state=SearchInfoState.photos)
    @func_logger
    def photos(call: CallbackQuery) -> None:
        """
        - сохраняется количество фотографий
        - /lowprice и /highprice:
         данные с API и вывод результата поиска

        - /bestdeal:
         минимальная цена за сутки
         вывод данных с API

        params:
        :call: callback
        """

        user_id: int = call.from_user.id
        chat_id: int = call.message.chat.id
        message_id: int = call.message.message_id

        if call.data == '0':
            text: str = 'Для отелей не будут выведены фотографии.'
        else:
            text: str = f'Для каждого отеля будет выведено фотографий: {call.data}'

        bot.edit_message_text(text, chat_id, message_id)
        logger.info(text)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['photos_amount'] = int(call.data)
            command: str = data['command']
            cur_data: dict = data

        hotels = None

        waiting_text: str = 'Пожалуйста, подождите...'
        if command == '/lowprice':
            bot.send_message(user_id, waiting_text)
            hotels: Optional[List[dict]] = find_lowprice(cur_data)
            hotels: Optional[List[dict]] = hotel_details(hotels,
                                                        cur_data['photos_amount'])
        elif command == '/highprice':
            bot.send_message(user_id, waiting_text)
            hotels: Optional[List[dict]] = find_highprice(cur_data)
            hotels: Optional[List[dict]] = hotel_details(hotels,
                                                        cur_data['photos_amount'])

        if command == '/bestdeal':
            bot.set_state(user_id, SearchInfoState.min_price, chat_id)
            bot.send_message(user_id, 'Укажите минимальную цену за сутки ')
        elif hotels:
            bot.set_state(user_id, SearchInfoState.result, chat_id)
            date_in = datetime.strptime(cur_data['date_in'], '%d.%m.%Y')
            date_out = datetime.strptime(cur_data['date_out'], '%d.%m.%Y')
            days = (date_out - date_in).days
            result_output(hotels, cur_data['user_id'], days)
            cur_data['hotels'] = hotels
            write_data(cur_data)
            logger.info('Поиск успешно завершен')
        else:
            text = 'Похоже произошла ошибка! ' \
                   '\nПопробуйте позже или установите другие параметры поиска'
            logger.warning('Поиск закончился с ошибкой')
            bot.send_message(user_id, text)


    @bot.message_handler(state=SearchInfoState.min_price)
    @func_logger
    def get_min_price(message: Message) -> None:
        """
        сохраняется минимальная цена за сутки
        запрашивается максимальная цена за сутки

        params:
        :message: сообщение
        """

        user_id: int = message.from_user.id
        chat_id: int = message.chat.id

        if not message.text.isdigit():
            text: str = 'Нужно указать целое число.\nПопробуйте еще раз.' \
                        '\nУкажите минимальную цену за сутки'
            bot.send_message(user_id, text)
        else:
            logger.info(f'Минимальная цена за сутки: {message.text}')
            bot.set_state(user_id, SearchInfoState.max_price, chat_id)
            bot.send_message(user_id,
                             'Укажите максимальную цену за сутки')
            with bot.retrieve_data(user_id, chat_id) as data:
                data['min_price'] = int(message.text)


    @bot.message_handler(state=SearchInfoState.max_price)
    @func_logger
    def get_max_price(message: Message) -> None:
        """
        сохраняется максимальная цена за сутки
        запрашиваются данные с API и выводятся результаты поиска

        params:
        :message: сообщение
        """

        user_id: int = message.from_user.id
        chat_id: int = message.chat.id
        with bot.retrieve_data(user_id, chat_id) as data:
            min_price = data['min_price']

        if not message.text.isdigit():
            text: str = 'Нужно указать целое число.\nПопробуйте еще раз.' \
                        '\nУкажите максимальную цену за сутки'
            bot.send_message(user_id, text)
        elif min_price >= int(message.text):
            text: str = 'Максимальная цена за сутки должна быть больше ' \
                        'минимальной.\n Попробуйте еще раз.' \
                        '\nУкажите максимальную цену за сутки'
            bot.send_message(user_id, text)
        else:
            logger.info(f'Максимальная цена за сутки: {message.text}')
            with bot.retrieve_data(user_id, chat_id) as data:
                data['max_price'] = int(message.text)
                cur_data: dict = data
            bot.send_message(user_id, 'Пожалуйста, подождите...')

            hotels: Optional[List[dict]] = find_bestdeal(cur_data)
            hotels: Optional[List[dict]] = hotel_details(hotels, cur_data['photos_amount'])

            if hotels:
                bot.set_state(user_id, SearchInfoState.result, chat_id)
                date_in = datetime.strptime(cur_data['date_in'], '%d.%m.%Y')
                date_out = datetime.strptime(cur_data['date_out'], '%d.%m.%Y')
                days = (date_out - date_in).days
                result_output(hotels, cur_data['user_id'], days)
                cur_data['hotels'] = hotels
                write_data(cur_data)
                logger.info('Поиск успешно завершен')
            else:
                text = 'Похоже ничего не нашлось, или произошла ошибка! ' \
                       '\nПопробуйте позже или установите другие параметры поиска'
                bot.send_message(user_id, text)
                logger.warning('Поиск закончился с ошибкой')


    """handler для команды /history"""
    @bot.message_handler(commands=['history'])
    @func_logger
    def history(message: Message) -> None:
        """
        Выводится история поисков отелей

        params:
        :message: сообщение
        """

        logger.info(f'Команда: {message.text}')
        user_id: int = message.from_user.id
        chat_id: int = message.chat.id
        logger.info(f'user_id = {user_id}; chat_id = {chat_id}')

        hotels_searches = hotels_history_from_db(user_id)

        if hotels_searches:
            bot.send_message(user_id, f'Запросов в истории поисков найдено: '
                                      f'{len(hotels_searches)}')
            bot.set_state(user_id, get_hotels_search, chat_id)
            hotels_searches_output(hotels_searches, user_id)
        else:
            bot.send_message(user_id, 'Вы еще не пользовались поиском!')


    @bot.callback_query_handler(func=None, state=get_hotels_search)
    @func_logger
    def get_hotels_from_history(call: CallbackQuery) -> None:
        """
        Выводятся результаты поиска отелей для конкретного поиска из истории

        params:
        call: обратный вызов
        """
        user_id: int = call.from_user.id
        hotels_search_id = int(call.data)

        hotels_search = HotelsSearch.get_by_id(hotels_search_id)
        hotels = hotels_data_from_db(hotels_search)
        days = days_in_hotels_from_db(hotels_search)
        result_output(hotels, user_id, days)

    """handler для неизвестных сообщений"""
    @bot.message_handler(state=None)
    def bot_echo(message: Message):
        text = ['Сообщение не распознано! Попробуйте команду /help']
        bot.reply_to(message, '\n'.join(text))


    bot.infinity_polling()

