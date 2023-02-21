import book
import dates
import datetime



class LoanError(Exception):
    pass
class BookLateError(LoanError):
    pass
class BookAlreadyLoanedError(LoanError):
    message = "Book is already loaned"

class BookNotOnLoanError(LoanError):
    message = "error, book was not loaned, recheck information or apprehend customer and call 911 \n disregard, swat team was called"

class BookReturnLateError(LoanError):
    message = "YOU ARE LATE TO RETURN THE BOK, DETH SHALL COME UPON YOU"

class IncorrectCustomerIdError(LoanError):
        message = "Incorrect Customer Id for this book, please check again"





class Loan:

    def __init__(self, book, customer_id, book_id):
        self.book = book
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = None
        self.return_date = None
        self.is_late: bool = None
        self.days_late = None
        self.actual_return_date = None
        self.extension = 0


    def __str__(self):
        pass

    ###getters###

    def get_book(self):
        return self.book
    def get_loaner_id(self):
        return self.customer_id

    def get_loaned_book_id(self):
        return self.book_id

    def get_loan_date(self):
        return self.loan_date

    def get_return_date(self):
        return self.return_date

    def get_is_late(self):
        return self.is_late

    def get_how_many_days_late(self):
        return self.days_late

    def get_actual_return_date(self):
        return self.actual_return_date

    def get_extension_length(self):
        return self.extension



    ###setters###

    def set_loan_date(self, man_date):
        # self.loan_date = dates.format_date_to_dmy(man_date)
        self.loan_date = man_date
    def set_loan_date_today(self):
        self.loan_date = dates.todays_date()

    def update_loan_date(self, new_date):
        # self.loan_date = dates.format_date_to_dmy(new_date)
        self.loan_date = new_date


    def set_return_date(self, return_date):
        # self.return_date = dates.format_date_to_dmy(return_date)
        self.return_date = return_date
    def set_is_late(self, is_late:bool):
        self.is_late = is_late
    def extend_loan_time(self, how_many_days):
        self.return_date = dates.todays_date()
        return_date_datetime_format = datetime.datetime.strptime(self.return_date, "%d/%m/%y")
        self.return_date = return_date_datetime_format + datetime.timedelta(days=int(how_many_days))
        self.return_date = datetime.datetime.strftime(self.return_date, "%d/%m/%y")
        self.extension = how_many_days
        return self.return_date

    # def set_return_date_via_type(self, book: object): #I HAVE A PYCHARM BUG WITH NO ABILITY TO DEBUG STRPTIME
    #     days_by_type = book.max_loan_length()
    #     loan_date_datetime_format = datetime.datetime.strptime(self.loan_date, "%d/%m/%y")
    #     self.return_date = loan_date_datetime_format + datetime.timedelta(days=days_by_type)
    #     self.return_date = datetime.datetime.strftime(self.return_date, "%d/%m/%y")

    def set_return_date_via_type(self, book):
        days_by_type = book.max_loan_length()
        loan_day, loan_month, loan_year = map(int, self.loan_date.split("/"))
        year, month, day = loan_year + 2000, loan_month, loan_day
        loan_date = datetime.date(year, month, day)
        return_date = loan_date + datetime.timedelta(days=days_by_type)
        self.return_date = return_date.strftime("%d/%m/%y")

    def set_return_custom_date(self, date: "format yyyy-mm-dd"):
        self.return_date = datetime.date(dates.format_date_to_dmy(date))

    def calculate_late_days(self):
        return_date = datetime.datetime.strptime(self.return_date, '%d/%m/%y')
        todays_date = datetime.datetime.strptime(dates.todays_date(), '%d/%m/%y')
        late_days = (return_date - todays_date).days
        if late_days <= 0:
            return 0
        else:
            return late_days

def same_loaner(customer_id, last_loaner_id):
    if customer_id == last_loaner_id:
        return True
    else:
        return False

def check_if_late(selected_book, loan_instance):  # check for late
    today_date = datetime.datetime.strptime(dates.todays_date(), '%d/%m/%y')
    return_date = datetime.datetime.strptime(loan_instance.get_return_date(), '%d/%m/%y')
    # today_date = datetime.datetime.strptime(dates.todays_date(), '%d/%m/%y')
    # return_date = selected_book.return_date
    duration = return_date - today_date
    if duration < datetime.timedelta(days=0):
        return True
    else:
        return False


