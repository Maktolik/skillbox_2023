from typing import Dict, Optional, List
import json

from commands.APIrequests import request_to_api
from commands.get_values_from_dict import get_values_from_dict
from config_data.config import RAPID_API_KEY, USD
from logs.loggers import func_logger


@func_logger
def find_hotel(city_id: str,
                   date_in: str,
                   date_out: str,
                   hotels_amount: int,
                   sort_type: Optional[str] = None,
                   min_price: Optional[int] = None,
                   max_price: Optional[int] = None
                   ) -> Optional[List[Dict[str, str]]]:
    """
    Производит поиск отелей

    params:
    :city_id: id города
    :date_in: дата заезда в отель
    :date_out: дата отъезда из отеля
    :hotels_amount: количество отелей
    :sort_type: тип сортировки отелей
    :min_price: минимальная цена отеля за сутки
    :max_price: максимальная цена отеля за сутки

    :return: список отелей
    """
    url = 'https://hotels4.p.rapidapi.com/properties/v2/list'
    day_in, month_in, year_in = map(int, date_in.split('.'))
    day_out, month_out, year_out = map(int, date_out.split('.'))

    payload = {
        'currency': 'USD',
        'eapid': 1,
        'locale': 'ru_RU',
        'siteId': 300000001,
        'destination': {'regionId': city_id},
        'checkInDate': {
            'day': day_in,
            'month': month_in,
            'year': year_in
        },
        'checkOutDate': {
            'day': day_out,
            'month': month_out,
            'year': year_out
        },
        "rooms": [
            {
                "adults": 1
            }
        ],
        'resultsStartingIndex': 0,
        'resultsSize': int(hotels_amount),
        'sort': 'PRICE_LOW_TO_HIGH'
    }
    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
    }

    if min_price and max_price:
        min_price /= USD
        max_price /= USD
        if min_price < 5:
            min_price = 5
        payload['filters'] = {
            'price': {
                'max': max_price,
                'min': min_price
            }
        }

    if sort_type:
        payload['sort'] = sort_type

    response = request_to_api(method='POST', url=url, headers=headers,
                              json=payload)
    if response:
        result = json.loads(response)
        result = get_values_from_dict(result,
                                     ['data', 'propertySearch', 'properties'])
        if result is None:
            return None

        hotels = list()
        for hotel in result:
            hotels.append({
                'hotel_id': hotel.get('id'),
                'hotel': hotel.get('name'),
                'price': float(
                    get_values_from_dict(hotel, ['price', 'lead', 'amount'])
                ) * USD,
                'distance': float(
                    get_values_from_dict(
                        hotel, ['destinationInfo', 'distanceFromDestination',
                                'value'])) * 0.621371
            })
        return hotels


@func_logger
def find_lowprice(data: dict) -> Optional[List[dict]]:
    """
    Поиск самых дешевых отелей

    params:
    :data: данные для поиска

    :return: список отелей
    """
    return find_hotel(
        data['city_id'],
        data['date_in'],
        data['date_out'],
        data['hotels_amount']
    )


@func_logger
def find_highprice(data: dict) -> Optional[List[dict]]:
    """
    Поиск самых дорогих отелей

    params:
    :data: данные для поиска

    :return: список отелей
    """
    hotels: List[dict] = find_hotel(
        data['city_id'],
        data['date_in'],
        data['date_out'],
        data['hotels_amount'],
        'DISTANCE'
    )
    return sorted(hotels, key=lambda elem: elem['price'], reverse=True)


@func_logger
def find_bestdeal(data: dict) -> Optional[List[dict]]:
    """
    Поиск отелей наиболее подходящих по цене
     и расположению от центра

    params:
    :data: данные для поиска

    :return: список отелей
    """
    hotels: List[dict] = find_hotel(
        data['city_id'],
        data['date_in'],
        data['date_out'],
        data['hotels_amount'],
        'DISTANCE',
        data['min_price'],
        data['max_price']
    )
    return hotels
