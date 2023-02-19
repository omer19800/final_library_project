import book
import loan
import loan as l
import dates
import logger
import datetime





class Library:

    def __init__(self):
        pass

    @staticmethod
    def loan_a_book(book_id, customer_id):
        try:
            #confirming yet again log exists
            if not logger.check_log_exists():
                raise logger.LogNotFoundError

            #get the book object from the book file
            selected_book = logger.get_book_object_by_id(book_id)

            #if the book is loaned, show an error
            if selected_book.is_loaned is True : #book is loaned
                # need a function to update the log of that book
                raise l.BookAlreadyLoanedError("Book is already loaned, check loan details or try another book")

            #actually doing stuff
            selected_book.set_is_loaned(True)  # change the book status to loaned
            loan = l.Loan(selected_book, customer_id, book_id) #creating a loan instance
            loan.set_loan_date_today() #setting the loan date to today
            loan.set_return_date_via_type #setting the return date via the type of the book

            #writing to log
            logger.write_log({'type': 'loan', 'book_id': book_id, 'customer_id': customer_id,
            'loan_date': str(loan.loan_date), 'return_date': str(loan.return_date)})

        except:
            logger.LogNotFoundError("There was a problem locating one of the log files") or\
            l.BookAlreadyLoanedError("Book is already loaned, check loan details or try another book")


    @staticmethod
    def return_a_book(book_id, customer_id):
        try:
            # confirming yet again log exists
            if not logger.check_log_exists():
                raise logger.LogNotFoundError

            # get the book object from the book file
            selected_book = logger.get_book_object_by_id(book_id)

            #confirm book is loaned
            if selected_book.is_loaned is True:  # book is loaned
                if l.check_for_same_loaner(customer_id, logger.get_last_loaner_id(book_id)) is False:
                    raise l.IncorrectCustomerIdError("Problem: Loaning Customer and Returning Customer are not the same")
            else:
                raise l.BookNotOnLoanError("Problem: Book was not on loan, recheck details or apprehend customer")

            #the return itself
            selected_book.set_is_loaned(False)  # change the book status to not loaned
            #need a function to update the log of that book
            loan_instance = logger.get_loan_object_by_id(selected_book, book_id, customer_id)  # get the loan object

            #check for late & write to the log
            if loan.check_if_late():
                late_days = loan_instance.calculate_late_days()
                loan_instance.set_is_late(True)
                log_entry = {'type': 'return', 'book_id': book_id, 'customer_id': customer_id,
                        'return_date': dates.todays_date(), 'status': 'Late',
                        'original_return_date': loan_instance.get_return_date , 'days_late': late_days }
                logger.write_log(log_entry)
                raise l.BookLateError("Problem: Book is late")

            #write to the log normal return
            log_entry = {'type': 'return', 'book_id': book_id, 'customer_id': customer_id,
                        'return_date': dates.todays_date(), 'status': 'returned on time'}
            logger.write_log(log_entry)

        except l.BookNotOnLoanError as e:
            print("Book was returned late, fine is due, 5000$")


#need function create customer
#need function add a book

Library.return_a_book(10, 80085)


