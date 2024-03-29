from typing import Dict, Optional, List
import json

from commands.APIrequests import request_to_api
from commands.get_values_from_dict import get_values_from_dict
from config_data.config import RAPID_API_KEY
from logs.loggers import func_logger


@func_logger
def hotel_details(hotels: List[dict], photos_amount: int) \
        -> Optional[List[dict]]:
    """
    Дополняет данные по отелям адресом и фотографиями

    params:
    :hotels: список отелей
    :photos_amount: количество фотографий

    :return: список отелей
    """
    if hotels is None:
        return None

    url = 'https://hotels4.p.rapidapi.com/properties/v2/detail'

    payload = {
        'currency': 'USD',
        'eapid': 1,
        'locale': 'ru_RU',
        'siteId': 300000001
    }
    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
    }

    for index, hotel in enumerate(hotels):
        payload['propertyId'] = hotel['hotel_id']
        response = request_to_api(method='POST', url=url, headers=headers,
                                  json=payload)
        hotels[index]['photos_list'] = list()
        address = None
        if response:
            result = json.loads(response)
            address = get_values_from_dict(result, ['data', 'propertyInfo',
                                                   'summary', 'location',
                                                   'address', 'addressLine'])
            images = get_values_from_dict(result, ['data', 'propertyInfo',
                                                  'propertyGallery', 'images'])
            if images is None:
                images = list()
            count = 0
            for image in images:
                count += 1
                if count > photos_amount:
                    break
                hotels[index]['photos_list'].append(image['image']['url'])

        hotels[index]['address'] = address

    return hotels
