"""
Модуль "входа" в программу.
"""
from login_register_form import choose_menu
from validation import isValid, usernameIsStrong, passwordIsStrong
from db_controller import add_user_to_table


# BUG: check_for_data_correct не проходит проверку.
#      1 ошибка - IndexError свящзана с обращением в базу данных и выкидывает тогда, когда идет проверка на перенос строки
#      2 ошибка - sqlite3.Error связана непонятно с чем. Иногда появляется, а иногда - нет...


def check_for_data_correct(data: tuple):
    username, password, form = data
    if form and username and password:
        if form is 'login':
            if isValid(username, password):
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
            return True
    else:
        return False


def main():
    data = choose_menu()
    if check_for_data_correct(data):
        print('govno!')
    else:
        print('ne govno')


if __name__ == "__main__":
    while True:
        a = main()
        if a is None:
            break

