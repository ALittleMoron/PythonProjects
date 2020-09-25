"""
модуль проверки введенных данных на правильность.
будет использоваться для паролей и имён пользователей
"""
import re

from db_controller import connect_to_database, user_from_table


def passwordIsStrong(password: str) -> bool:
    """ Возвращает True, если пароль сильный, иначе возвращает False.

    аргумент password -- пароль для проверки.
    """
    strong_patterns = [(re.compile(r'\w{8,}'), 'хотя бы 8 символов'),
                       (re.compile(r'[a-z]+'), 'хотя бы 1 символ в нижнем регистре.'),
                       (re.compile(r'[A-Z]+'), 'хотя бы 1 символ в верхнем регистре.'),
                       (re.compile(r'[0-9]+'), 'хотя бы 1 цифру.'),
                       (re.compile(r'[+-/*!&$#?=@<>]+'), 'хотя бы 1 специальный символ.')]

    for pattern, massage in strong_patterns:
        if type(pattern.fullmatch(password)) is None:
            print('\nПароль должен содержать' + massage)
            return False
        return True


def usernameIsStrong(username: str) -> bool:
    """ Возвращает True, если логин сильный, иначе возвращает False.

    аргумент username -- имя пользователя для проверки
    """

    strong_patterns = [(re.compile(r'\w{4,}'), 'хотя бы 4 символа.'),
                       (re.compile(r'\w[a-zA-Z]+'), 'хотя бы 1 латинскую букву')]

    for pattern, massage in strong_patterns:
        if type(pattern.fullmatch(username)) is None:
            print('\nИмя пользователя должно содержать' + massage)
            return False
        return True


def usernameInDatabase(username: str) -> bool:
    """ Возвращает True, если такой логин есть в базе данных, иначе возвращает False.

    аргумент username -- имя пользователя для проверки
    """
    try:
        db_username, _ = user_from_table(connect_to_database('users.db'),
                                                   username=username)
        return True
    except TypeError:
        return False


def isValid(username: str, hashed_password: str) -> bool:
    """ Возвращает True, если логин и хешированный пароль совпадают
    с данными в базе, иначе False.

    аргументы:
    username -- имя пользователя из формы
    hashed_password -- хешированный пароль из формы
    """
    try:
        db_username, db_password = user_from_table(connect_to_database('users.db'),
                                                   username=username)
        return username == db_username and hashed_password == db_password
    except (TypeError, IndexError):
        return False

if __name__ == "__main__":
    print(isValid('ALittleMoron', '35e62fd8f5625ff163456069159feb635d7063c9'))
