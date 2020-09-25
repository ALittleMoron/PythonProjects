"""
Модуль "входа" в программу.
"""
from hashlib import sha1
from typing import NoReturn

from db_controller import add_user_to_table, connect_to_database
from login_register_form import choose_menu
from validation import isValid, passwordIsStrong, usernameIsStrong


# BUG: check_for_data_correct не проходит проверку. (FIXED)


SALT = 'Salt for more secured data ' # используй совместно с паролем (SALT + password)


def check_for_data_correct(data: tuple):
    username, password, form = data
    hashed_password = sha1(bytes(SALT+password, encoding = 'utf-8')).hexdigest()
    if form and username and password:
        if form == 'login':
            if isValid(username, hashed_password):
                return True
            else:
                return False
        else:
            if not usernameIsStrong(username):
                print('\nМы не можем пропустить такое имя пользователя.\nОно слишком простое.\n\n')
                return False
            if not passwordIsStrong(password):
                print('\nМы не можем пропустить такой пароль.\nОн слишком слабый.\n\n')
                return False
            
            register_data = username, hashed_password
            add_user_to_table(connect_to_database('users.db'), register_data)
            return True
    else:
        return False


def main() -> bool:
    data = choose_menu()
    if check_for_data_correct(data):
        print('Класс, вы это сделали!')
        return None
    else:
        print('Либо логин, либо пароля не правильный... Попробуй ещё раз\n\n')
        return True


if __name__ == "__main__":
    while True:
        a = main()
        if a is None:
            break
