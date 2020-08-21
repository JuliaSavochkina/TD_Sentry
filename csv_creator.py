import csv


def csv_creator(name: str, data: list) -> None:
    """
    Создает файл с именем name и
    :param name: Название будущего файла.
    :param data: Список, содержит номер заказа/uid/дату заказа
    """
    with open(name, 'a') as File:
        writer = csv.writer(File)
        writer.writerow(data)
