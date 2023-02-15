import book
import loan
import dates
import logger
import datetime


def check_if_book_is_loaned(book_id):
    logger.check_for_lines_with(book_id)



class Library:

    def __init__(self):
        pass

    def loan_a_book(self, book_id, customer_id):
        if logger.check_log_exists():
            raise logger.LogNotFoundError
        else:
            if check_if_book_is_loaned(book_id) is True: #book is loaned
                raise loan.BookAlreadyLoanedError("Book is already loaned, check loan details or try another book")
            elif check_if_book_is_loaned(book_id) is False: #book is not loaned
                pass


