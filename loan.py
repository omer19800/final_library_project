import book
import dates
import datetime
import logger
from logger import LogNotFoundError
from typing import List


class LoanError(Exception):
    pass

class BookAlreadyLoanedError(LoanError):
    message = "Book is already loaned"

class BookNotOnLoanError(LoanError):
    message = "error, book was not loaned, recheck information or apprehend customer and call 911 \n disregard, swat team was called"

class BookReturnLateError(LoanError):
    message = "YOU ARE LATE TO RETURN THE BOK, DETH SHALL COME UPON YOU"

class IncorrectCustomerIdError(LoanError):
        message = "Incorrect Customer Id for this book, please check again"


log = logger.Log()


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
        self.loan_date = dates.format_date_dmy(man_date)

    def set_loan_date_today(self):
        self.loan_date = dates.todays_date()

    def update_loan_date(self, new_date):
        self.loan_date = dates.format_date_dmy(new_date)

    def extend_loan_time(self, how_many_days):
        self.return_date = dates.todays_date()
        return_date_datetime_format = datetime.datetime.strptime(self.return_date, "%d/%m/%y")
        self.return_date = return_date_datetime_format + datetime.timedelta(days=int(how_many_days))
        self.return_date = datetime.datetime.strftime(self.return_date, "%d/%m/%y")
        self.extension = how_many_days
        return self.return_date

    def set_return_date_via_type(self, book: object):
        days_by_type = book.max_loan_length()
        loan_date_datetime_format = datetime.datetime.strptime(self.loan_date, "%d/%m/%y")
        self.return_date = loan_date_datetime_format + datetime.timedelta(days=days_by_type)
        self.return_date = datetime.datetime.strftime(self.return_date, "%d/%m/%y")
        return self.return_date

    def set_return_custom_date(self, date: "format yyyy-mm-dd"):
        self.return_date = datetime.date(dates.format_date_dmy(date))


def check_if_book_is_loaned_logs(book_id):
    relevant_logs = logger.check_for_lines_with(book_id)
    if relevant_logs[-1]["Loaned"]:
        return True
    else:
        return False


# book1 = book.Book(1, "sheesh", "pardo", 1999, 1)
# book2 = book.Book(2, "sheesh", "pardo", 1998, 2)
# book3 = book.Book(book_id = 1, name = 'The Great Gatsby', author = 'F. Scott Fitzgerald',year= 1991 , book_type= 1 )

# loan = Loan(book3, book3.book_id, 123)

# loan.loan_book(loan.book, loan.book_id, loan.customer_id)
# loan.return_book(loan.book, loan.book_id, loan.customer_id)
# loan.extend_loan_time(5)






        #centralized dump of all actions into the json through the log_entries = []
        # def loan_book(self, book, book_id, customer_id):
        #     # set loan date and return date
        #     log_entry = {'type': 'loan', 'book_id': book_id, 'customer_id': customer_id,
        #                  'loan_date': str(self.loan_date), 'return_date': str(self.return_date)}
        #     self.log_entries.append(Log(log_entry))

        # if book.get_loaned is False:
            # raise BookAlreadyLoaned