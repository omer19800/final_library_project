import book
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



    def return_a_book(self, book_id, customer_id):
        pass
        #first confirm book was loaned
        #second confirm from the book log that the currect customer took and returnes
        #third confirm that the correct book was returned - using book id
        #dates function to confirm return date is similar to expected return date
        #except is the if else statement of exceptions
        #possible - except BookReturnLateError: (then) call loan function to handle late return
        #after all is confirmed
            #set book status to False, update the book log
            #update the log with the return details + how much late, when was actually returrned


Library.loan_a_book(10, 80085)


