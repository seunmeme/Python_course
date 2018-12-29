import datetime

def print_header():
    print('-------------------------------------')
    print('             BIRTHDAY APP       ')
    print('-------------------------------------')
    print()


def get_user_birthday():
    print('When were you born')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    birthday = datetime.date(year, month, day)

    return birthday


def compute_days_between_dates(original_date, target_date):
    pass


def print_birthday_info():
    pass


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


#get_user_birthday()