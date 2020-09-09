"""
модуль проверки введенных данных на правильность.
будет использоваться для паролей и имён пользователей
"""
from hashlib import sha1
import re


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

if __name__ == "__main__":
    print(passwordIsStrong('Aagsagasg1!'))
    print(usernameIsStrong('Sasg'))
