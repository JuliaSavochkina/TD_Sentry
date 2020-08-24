import requests
from typing import Generator

from keys import SENTRY_TOKEN


def get_data(issue_id: str) -> Generator:
    """
    Постранично опрашивает API Sentry по указанному issue_id, выгружая информацию по каждому event.
    Выделяет словарь из поля message ответа, из словаря забирает order_id/uid и дату заказа, если есть.
    Скрадывает построчно в csv файл.
    :param issue_id: номер ишью Sentry
    :returns: генератор с информацией одной страницы
    """
    headers: dict = {"Authorization": f"Bearer {SENTRY_TOKEN}"}
    results: str = 'true'
    params: dict = {}

    while results == 'true':
        response = requests.get(f'https://s.crutches.space/api/0/issues/{issue_id}/events/', params=params, headers=headers)
        yield response.json()

        pre_cursor: dict = response.headers
        cursor: str = pre_cursor['Link'].split(';')[-1].split('=')[-1].replace('"', '')
        results: str = pre_cursor['Link'].split(';')[-2].split('=')[-1].replace('"', '')
        params.update({'cursor': cursor})
