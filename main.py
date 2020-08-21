from get_data import get_data


if __name__ == '__main__':
    issue_id = 'issue_id'
    type_of_search = 'order_id'  # uid или order_id
    name = 'name.csv'
    get_data(issue_id, type_of_search, name)
