from colorama import init
init()
from colorama import Fore
def calculate_salary():
    salary_dict = {'sys_admin' : 65000, 'data_science' : 70000, 'developer' : 69000}
    sum_salary = 0
    for key, value in salary_dict.items():
        sum_salary += value
    avarage_salary = sum_salary / len(salary_dict)
    return print(f'Средняя заработная плана: {avarage_salary}')

calculate_salary()