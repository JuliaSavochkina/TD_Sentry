import json
from typing import Generator


def extract_info(type_of_search: str, response_json: Generator) -> set:
    """
    Получает на вход генератор с информацией одной страницы выдачи API. Достает для каждого event type_of_search и дату
    дейсвтия, если таковая имеется. Складывает в множество, чем гарантируется уникальность event'ов.
    :param type_of_search: какое значение будет содержаться в ысм файле (пока это order_id или uid)
    :param response_json: генератор с информацией одной страницы, получаем из get_data
    :return: множество кортежей, одни кортеж - уникальное значение действия + дата (опционально)
    """
    data: set = set()
    for issue in response_json:
        message: str = issue[0]['message']
        order_info: str = message.split('uid\n')[1]
        order: str = order_info.rstrip()
        try:
            order_date: str = json.loads(order)["datetime_action"]
        except KeyError:
            row: tuple = tuple([json.loads(order)[type_of_search]])
        else:
            row: tuple = tuple([json.loads(order)[type_of_search], order_date])

        data.add(row)
    return data
