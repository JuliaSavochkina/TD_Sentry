from csv_creator import csv_creator
from extract_info import extract_info
from get_data import get_data


def main(issue_id: str, type_of_search: str, name: str) -> None:
    """
    Обращается к API Sentry, забрает данные по указанному issue_id, для каждого issue формирует множество уникальных действий и передает в csv файл.
    :param issue_id: номер issue
    :param type_of_search: пока order_id или uid, это значение будет отображаться в первом столбце файла
    :param name: название файла
    """
    data_from_api = get_data(issue_id)
    uniq_events = extract_info(type_of_search, data_from_api)
    for event in uniq_events:
        csv_creator(name, list(event))


if __name__ == '__main__':
    ISSUE_ID = 'issue_id'
    TYPE_OF_SEARCH = 'order_id'  # uid или order_id
    NAME = 'name.csv'
    main(ISSUE_ID, TYPE_OF_SEARCH, NAME)
