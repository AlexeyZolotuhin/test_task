import datetime


def check_format_data(v: str):
    try:
        datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S%z')
    except ValueError:
        raise ValueError('Not a valid datetime string')
