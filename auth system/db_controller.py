"""
модуль управления базой данных sqlite3.
добавление пользователя, получение данных о нем для сравнения или удаление его
из базы данных.
"""
import os.path
import sqlite3


# как будет возвращен пользователь при запросе в бд.
User = (str, str)


def connect_to_database(database_name: str, path: str = '') -> sqlite3.Connection:
    """ Функция подключения к базе данных. Возвращает соединение на уже
    существующую базу данных (Не хочу случайно создать лишнюю БД).

    аргументы:
    database_name -- файл базы данных
    path -- путь к файлу базы данных (Опциональный. Не передавать аргумент,
    если база данных находится рядом с python файлом.
    """
    try:
        database = os.path.join(path, database_name)
        if os.path.isfile(database) and ('.db' in database or '.sqlite' in database):
            connection = sqlite3.connect(database, timeout=5)
            return connection
        else:
            return None
    except sqlite3.Error as e:
        print(e)
        connection.close()


def add_user_to_table(connection: sqlite3.Connection,
                      data: tuple) -> None:
    """ Функция добавления информации в имеющуюся таблицу в базе данных

    аргументы:
    connection -- соединение с базой данных
    data -- данные пользователя вида (username, password (уже хешированный))
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO users VALUES (?, ?)""", data)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def delete_info_in_table(connection: sqlite3.Connection,
                         table_name: str, username: int) -> None:
    """ Функция удаляет запись в таблице по её id

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    username -- имя пользователя
    """
    pass


def user_from_table(connection: sqlite3.Connection,
                    username: str) -> User:
    """ Функция возвращает пользователя по его имени

    аргументы:

    connection -- соединение с базой данных
    username -- имя пользователя
    """
    username += '\n'
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        cursor = connection.cursor()
        cursor.execute("""SELECT username, password FROM users
                          WHERE username = ?""", (username,))
        data = cursor.fetchall()[0]
        if '\n' in data[0] and '\n' in data[1]:
            normalized_user = tuple([user[:-1] for user in data])
        else:
            normalized_user = data
        return normalized_user
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


if __name__ == "__main__":
    b = ('asgasg', 'sagasg')
    add_user_to_table(connect_to_database('users.db'), b)
