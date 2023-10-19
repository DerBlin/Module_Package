if __name__ == "__main__":
    from datetime import datetime, date, time
    from application.salary import calculate_salary
    from application.db.people import get_employees
    from colorama import init
    init()
    from colorama import Back

    print(Back.BLUE + f'{datetime.now()}')


