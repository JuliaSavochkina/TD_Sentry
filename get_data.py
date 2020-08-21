import json

import requests

from csv_creator import csv_creator
from keys import SENTRY_TOKEN


def get_data(issue_id: str, type_of_search: str, name: str) -> None:
    """
    Постранично опрашивает API Sentry по указанному issue_id, выгружая информацию по каждому event.
    Выделяет словарь из поля message ответа, из словаря забирает order_id/uid и дату заказа, если есть.
    Скрадывает построчно в csv файл.
    :param issue_id: номер ишью Sentry
    :param type_of_search: что будет отображаться в файле. Пока есть два варианта order_id и uid. По запросу можно
    добавить оба.
    :param name: Название будущего файла.
    """
    headers = {"Authorization": f"Bearer {SENTRY_TOKEN}"}
    results = 'true'
    params = {}
    data = set()
    while results == 'true':
        request = requests.get(f'https://s.crutches.space/api/0/issues/{issue_id}/events/', params=params, headers=headers)
        r = request.json()

        for issue in r:
            s = issue['message']
            order_info = s.split('uid\n')[1]
            order = order_info.rstrip()
            try:
                order_date = json.loads(order)["datetime_action"]
            except KeyError:
                row = tuple([json.loads(order)[type_of_search]])
            else:
                row = tuple([json.loads(order)[type_of_search], order_date])

            data.add(row)

        pre_cursor = request.headers
        cursor = pre_cursor['Link'].split(';')[-1].split('=')[-1].replace('"', '')
        results = pre_cursor['Link'].split(';')[-2].split('=')[-1].replace('"', '')
        params.update({'cursor': cursor})

    for item in data:
        csv_creator(name, list(item))
