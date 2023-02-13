import datetime


def todays_date():
    today_date = datetime.date.today()
    formatted_today = datetime.datetime.strftime(today_date, "%d/%m/%y")
    return formatted_today

def current_time():
    current_time = datetime.datetime.now()
    formatted_current_time = current_time.strftime("%H:%M:%S")
    return formatted_current_time

def format_date_dmy(date):
    if len(date.split("/")[0]) == 4:
        formatted_date = datetime.datetime.strptime(date, '%Y/%m/%d').strftime('%d/%m/%y')
    elif len(date.split("/")[0]) == 2:
        formatted_date = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%d/%m/%y')
    return formatted_date

# dates method to ranslate from normal date method to datetime.date formar yyyy-mm-dd
# def format_date_ymd(date):
#     fixed_format_date = date.strftime("%Y-%m-%d")
#     return fixed_format_date

# def into_datetime_object(date):
#     turned_date = datetime.strptime(date, "%d").date()
#     return turned_date


