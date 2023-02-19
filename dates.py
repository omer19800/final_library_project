import datetime


def todays_date():
    today_date = datetime.date.today()
    formatted_today = datetime.datetime.strftime(today_date, "%d/%m/%y")
    return formatted_today

def current_time(): #not in use, was an idea
    current_time = datetime.datetime.now()
    formatted_current_time = current_time.strftime("%H:%M:%S")
    return formatted_current_time

def format_date_to_dmy(date): #function to take a date and format it into dd/mm/yy
    if len(date.split("/")[0]) == 4:
        formatted_date = datetime.datetime.strptime(date, '%Y/%m/%d').strftime('%d/%m/%y')
    elif len(date.split("/")[0]) == 2:
        formatted_date = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%d/%m/%y')
    return formatted_date

def format_date_to_ymd(date): #function to take a date and to make it a datetime acceptable format
    date_obj = datetime.datetime.strptime(date, '%d/%m/%y')
    date_obj = date_obj.strftime('%Y-%m-%d')
    return date_obj




