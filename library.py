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

        #get the book object from the book file
        selected_book = logger.get_book_by_id(book_id)

        #if the book is loaned, show an error
        if loan.check_if_book_is_loaned_in_logs(book_id) is True and selected_book.is_loaned is True : #book is loaned
            raise loan.BookAlreadyLoanedError("Book is already loaned, check loan details or try another book")

        #confirm book is not loaned both in log and in object
        elif loan.check_if_book_is_loaned_in_logs(book_id) is False and selected_book.is_loaned is False : #book is not loaned

            loan.Loan()   #create a loan instance for the book and all messy functions
            #set the book loan time to today
            #calculate expected return time

            selected_book.set_is_loaned(True) #change the book status to loaned
            #function here to update the book status in the book log

            #{'type': 'loan', 'book_id': book_id, 'customer_id': customer_id,
            # 'loan_date': str(self.loan_date), 'return_date': str(self.return_date), 'extention' : int(self.extension)}

            logger.write_log() #old format - inherited from the chatgpt chat


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





