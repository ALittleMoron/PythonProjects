"""
модуль управления базой данных sqlite3.
добавление пользователя, получение данных о нем для сравнения или удаление его
из базы данных.
"""
import os.path
import sqlite3
from typing import NoReturn


# список того, что нужно доделать в этом модуле:
# TODO 1: написать функцию обновления таблицы, которая будет убирать перенос
#         строк ('username\n', 'password\n') -> ('username', 'password').


# как будет возвращен пользователь при запросе в бд.
User = (str, str)


class WrongDataBaseNameException(Exception):
    """ Класс-исключение для отлова ошибки о неправильном введенном названии БД """
    pass


def connect_to_database(database_name: str) -> sqlite3.Connection:
    """ Функция подключения к базе данных. Возвращает соединение на уже
    существующую базу данных (Не хочу случайно создать лишнюю БД).

    аргументы:
    database_name -- файл базы данных
    path -- путь к файлу базы данных (Опциональный. Не передавать аргумент,
    если база данных находится рядом с python файлом.
    """
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, database_name)
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(e)
        connection.close()


def create_users_table(connection: sqlite3.Connection) -> NoReturn:
    """ Функция создания таблицы в базе данных

    аргументы:
    connection -- соединение с базой данных
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        cursor = connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS "users"(
                               "username" TEXT NOT NULL UNIQUE,
                               "password" TEXT NOT NULL UNIQUE,
                               PRIMARY KEY("password"));""")
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def add_user_to_table(connection: sqlite3.Connection,
                      data: tuple) -> NoReturn:
    """ Функция добавления информации в имеющуюся таблицу в базе данных

    аргументы:
    connection -- соединение с базой данных
    data -- данные пользователя вида (username, password (уже хешированный))
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных.')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO users VALUES (?, ?)""", data)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def user_from_table(connection: sqlite3.Connection,
                    username: str) -> User:
    """ Функция возвращает пользователя по его имени

    аргументы:

    connection -- соединение с базой данных
    username -- имя пользователя
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных.')
        cursor = connection.cursor()
        cursor.execute("""SELECT username FROM users WHERE username = ?""", (username,))
        if cursor.fetchall() is None:
            return None
        cursor.execute("""SELECT username, password FROM "users"
                          WHERE username = ?""", (username,))
        try:
            data = cursor.fetchall()[0]
        except IndexError as e:
            print(e)
            return None
        return data

    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


if __name__ == "__main__":
    a=user_from_table(connect_to_database('users.db'), 'ALittleMoron')
    print(a)
