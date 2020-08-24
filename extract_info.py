import json
from typing import Generator

from get_data import get_data


def extract_info(type_of_search: str, issue_id: str) -> set:
    data: set = set()
    response_json: Generator = get_data(issue_id)
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

