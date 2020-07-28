import psycopg2
import os, os.path


class WrongDataBaseNameException(Exception):
    """ Класс-исключение для отлова ошибки о неправильном введенном названии БД """
    pass


def something():
    """"""
    pass


if __name__ == '__main__':
    a = os.environ['SQL_password']
    print(a, type(a))
