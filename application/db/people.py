from colorama import init
init()
from colorama import Fore

def get_employees():
    while True:
        answer = input('Введите имя пользователя:')
        if len(answer) == 0:
            print('Некорректное имя!')
        else:
            return print(f'Приветствую, {Fore.RED + answer}!')
               
get_employees()
