from customer import Customer
import loan as l
from book import *
import dates
import logger
import time





class Library:

    def __init__(self):
        pass

    @staticmethod
    def loan_a_book(book_id, customer_id):
        try:
            #confirming yet again log exists
            if not logger.check_log_exists():
                raise logger.LogNotFoundError("Problem : Log File Was Not Found")

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

            # need a function to update the log of that book
            logger.update_book_status(book_id, False) #chat

            # function to get customer instance
            logger.get_customer_instance_by_id(customer_id) #chat

            # a function to add the book to the customer
            customer.add_loaned_book_to_customer(book_id) #chat


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
                raise logger.LogNotFoundError("Problem : Log File Was Not Found")

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
            loan_instance = logger.get_loan_object_by_id(selected_book, book_id, customer_id)  # get the loan object

            # need a function to update the log of that book
            logger.update_book_status(book_id, False)  # update the book status to returned #chat

            # function to get customer instance
            logger.get_customer_instance_by_id(customer_id) #chat

            # a function to remove the book from the customer instance
            customer.remove_loaned_book_from_customer(book_id) #chat


            #check for late & write to the log
            if l.check_if_late():
                late_days = loan_instance.calculate_late_days()
                loan_instance.set_is_late(True)
                log_entry = {'type': 'return', 'book_id': book_id, 'customer_id': customer_id,
                        'return_date': dates.todays_date(), 'status': 'late',
                        'original_return_date': loan_instance.get_return_date , 'days_late': late_days }
                logger.write_log(log_entry)
                raise l.BookLateError("Problem: Book is being returned late")

            #write to the log normal return
            log_entry = {'type': 'return', 'book_id': book_id, 'customer_id': customer_id,
                        'return_date': dates.todays_date(), 'status': 'returned on time'}
            logger.write_log(log_entry)

        except l.BookNotOnLoanError as e:
            print("Book was returned late, fine is due, 5000$")

    @staticmethod#chat
    def select_a_customer(customer_id_num):
        selected_customer = customer.get_customer_instance_by_id(customer_id)
        return selected_customer
        #get a customer instance from the customer personal id num using a logger function
    @staticmethod
    def create_a_customer(id, name, email, birthday, city, street, house_num):
        customer = Customer(id, name, email, birthday, city, street, house_num)
        customer.add_to_customer_file()

    @staticmethod #chat
    def remove_a_customer(customer_id):
        #through the logger remove the customer based on the personal id num from the customer file
        logger.remove_a_customer_by_id(customer_id)

    @staticmethod
    def add_a_book(name, author, year, type=None):
        book = Book(book.generate_book_id(), name, author, year, type=None)
        book.add_book_to_library_stock()

    @staticmethod #chat
    def remove_a_book(book_id):
        #through the logger remove the book based on the book id
        logger.remove_book(book_id) #chat

def small_loading_animation():
    print('Loading', end="")
    for i in range(3):
        time.sleep(.5)
        print(".", end="")
    time.sleep(0.2)
    print("\n")

def small_processing_animation():
    print('Processing', end="")
    for i in range(3):
        time.sleep(.5)
        print(".", end="")
    time.sleep(0.2)
    print("\n")
# Library.return_a_book(10, 80085)


