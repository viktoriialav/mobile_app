from datetime import datetime

import config


def date_middle_format(value: datetime):
    expense_date = value.date().strftime('%b %d, %Y').split()
    expense_date[1] = expense_date[1][1:] if expense_date[1][0] == '0' else expense_date[1]
    expense_date = ' '.join(expense_date)
    return expense_date


def datetime_long_format(value: datetime):
    if config.settings.is_bstack:
        expense_datetime = value.strftime('%A, %B %d, %Y %H:%M').split()
    else:
        expense_datetime = value.strftime('%A, %B %d, %Y %I:%M %p').split()
    expense_datetime[2] = expense_datetime[2][1:] if expense_datetime[2][0] == '0' else expense_datetime[2]
    expense_datetime[4] = expense_datetime[4][1:] if expense_datetime[4][0] == '0' else expense_datetime[4]
    expense_datetime = ' '.join(expense_datetime)
    return expense_datetime


def date_and_time_in_datetime_form(date, time):
    if config.settings.is_bstack:
        return datetime.strptime(f'{date} {time}', '%m/%d/%y %H:%M')
    return datetime.strptime(f'{date} {time}', '%m/%d/%y %I:%M %p')
