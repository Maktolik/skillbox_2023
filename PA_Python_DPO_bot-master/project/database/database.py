"""
Мудуль отвечает за взаимодействия с бд
"""

from datetime import datetime
from typing import List, Optional
import os

from peewee import SqliteDatabase, Model, CharField, IntegerField, \
    ForeignKeyField, DateTimeField, FloatField, DateField

from logs.loggers import func_logger


db = SqliteDatabase(os.path.join('database', 'bot_database.db'))


class BaseModel(Model):
    """"Класс базовой модели для ORM"""

    class Meta:
        database: SqliteDatabase = db


class User(BaseModel):
    """
    Класс Пользователь

    Attributes:
    name - имя пользователя
    user_id - id пользователя
    chat_id - id чата
    """

    name = CharField()
    user_id = IntegerField(unique=True)
    chat_id = IntegerField()


class HotelsSearch(BaseModel):
    """
    Класс Поиск отелей

    Attributes:
    command - команда для поиска
    user - пользователь
    date_time - дата и время начала поиска
    city - место для поиска
    city_id - id места для поиска
    date_in - дата заезда
    date_out - дата отъезда
    hotels_amount - количество отелей
    photos_amount - количество фотографий
    min_price - мин цена за сутки
    max_price - макс цена за сутки
    """

    command = CharField()
    user = ForeignKeyField(User, backref='Searches')
    date_time = DateTimeField()
    city = CharField()
    city_id = CharField()
    date_in = DateField()
    date_out = DateField()
    hotels_amount = IntegerField()
    photos_amount = IntegerField()
    min_price = IntegerField(null=True)
    max_price = IntegerField(null=True)


class Hotel(BaseModel):
    """
    Класс Отель

    Attributes:
    hotels_search - поиск отелей
    name - название отеля
    hotel_id - id отеля
    address - адрес отеля
    distance - расстояние от отеля до центра
    price - цена за сутки проживания в отеле
    """

    hotels_search = ForeignKeyField(HotelsSearch, backref='hotels')
    name = CharField()
    hotel_id = IntegerField()
    address = CharField()
    distance = FloatField()
    price = FloatField()


class Photo(BaseModel):
    """
    Класс Фото

    Attributes:
    hotel - отель
    url - ссылка на сайт отеля
    """

    hotel = ForeignKeyField(Hotel, backref='photos')
    url = CharField()


@func_logger
def create_tables():
    """Создает таблицы в базе данных"""

    with db:
        db.create_tables([User, HotelsSearch, Hotel, Photo])


@func_logger
def write_data(data: dict) -> None:
    """
    Записывает данные в базу данных атомик режим

    params:
    :data: словарь с данными
    """

    with db.atomic():
        user = User.get_or_create(
            name=data['user_name'],
            user_id=data['user_id'],
            chat_id=data['chat_id']
        )[0]

        hotels_search = HotelsSearch.create(
            command=data['command'],
            user=user,
            city=data['city'],
            city_id=data['city_id'],
            date_time=datetime.strptime(data['date_time'], '%d.%m.%Y %H:%M:%S'),
            date_in=datetime.strptime(data['date_in'], '%d.%m.%Y'),
            date_out=datetime.strptime(data['date_out'], '%d.%m.%Y'),
            hotels_amount=data['hotels_amount'],
            photos_amount=data['photos_amount'],
            min_price=data.get('min_price'),
            max_price=data.get('max_price')
        )

        for i_hotel in data['hotels']:
            hotel = Hotel.create(
                    hotels_search=hotels_search,
                    name=i_hotel['hotel'],
                    hotel_id=i_hotel['hotel_id'],
                    address=i_hotel['address'],
                    distance=i_hotel['distance'],
                    price=i_hotel['price']
            )
            for photo in i_hotel['photos_list']:
                Photo.create(hotel=hotel, url=photo)


@func_logger
def hotels_history_from_db(user_id: int) -> List[HotelsSearch]:
    """
    Выводит из базы данных историю поисков отелей

    params:
    :user_id: id пользователя

    :return: история поисков отелей
    """

    with db.atomic():
        query = HotelsSearch.select().join(User).where(User.user_id == user_id)
    query: list = list(query)

    return query


@func_logger
def hotels_photos_from_db(hotel: Hotel) -> List[Optional[str]]:
    """
    Выводит из базы данных фотографии для отеля

    params:
    :hotel: отель

    :return: список с ссылками на фотографии
    """

    photos_list = list()
    with db.atomic():
        if hotel.hotels_search.photos_amount:
            photos_list = [
                photo.url
                for photo in
                Photo.select().where(Photo.hotel == hotel)
            ]

    return photos_list


@func_logger
def hotels_data_from_db(hotels_search: HotelsSearch) -> list:
    """
    Выводит из базы данных данные по отелям

    params:
    :hotels_search: поиск отелей

    :return: список с данными по отелям
    """

    with db.atomic():
        query = Hotel.select().where(Hotel.hotels_search == hotels_search)

    hotels = list()
    for hotel in query:
        hotels.append({
            'hotel': hotel.name,
            'hotel_id': hotel.hotel_id,
            'address': hotel.address,
            'distance': hotel.distance,
            'price': hotel.price,
            'photos_list': hotels_photos_from_db(hotel)
        })

    return hotels


@func_logger
def days_in_hotels_from_db(hotels_search: HotelsSearch) -> int:
    """
    Определяет по данным из поиска отелей количество дней
    бронирования отеля

    params:
    :hotels_search: поиск отелей

    :return: количество дней бронирования
    """

    return (hotels_search.date_out - hotels_search.date_in).days
