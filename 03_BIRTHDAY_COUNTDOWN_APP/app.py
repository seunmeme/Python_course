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
    # The line of code below handles the logic that allows us get a usable date differnce.
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date

    return dt.days

def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days time'.format(days))
    else:
        print('Happy Birthday!!!')


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


main()