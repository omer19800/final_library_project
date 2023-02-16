import book
import loan
import dates
import logger
import datetime





class Library:

    def __init__(self):
        pass

    def loan_a_book(self, book_id, customer_id):
        if not logger.check_log_exists():
            raise logger.LogNotFoundError


        selected_book = book.Book(book.get_book_by_id(book_id))


        if loan.check_if_book_is_loaned_logs(book_id) is True and selected_book.is_loaned is True : #book is loaned
            raise loan.BookAlreadyLoanedError("Book is already loaned, check loan details or try another book")

        elif loan.check_if_book_is_loaned_logs(book_id) is False and selected_book.is_loaned is True : #book is not loaned
            loan.Loan()
            selected_book.set_is_loaned(True)
            logger.write_log() #old format




