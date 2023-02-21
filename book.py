import json
import random

class BookError(Exception):
    pass
class DoubleBookIdError(BookError):
    pass

class BookOnLoanError(BookError):
    pass




class Book:

    def __init__(self, book_id: int, name: str, author: str, year: int, book_type:int= random.randint(1,3)) -> object:
        self.book_id = book_id
        self.name = name
        self.author = author
        self.year = year
        self.book_type = book_type
        self.loaned: bool = False

    def __str__(self):
        pass

    def get_book_id(self):
        return self.book_id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_publish_year(self):
        return self.year

    def get_type(self):
        if not self.book_type:
            self.book_type = random.randint(1, 3)
        return self.book_type


    def max_loan_length(self):
        book_type = self.book_type
        if book_type == 1:
            days = 10
        elif book_type == 2:
            days = 5
        elif book_type == 3:
            days = 2
        return days

    def is_loaned(self):
        return self.loaned

    def set_loaned_or_not(self, status:bool):
        self.loaned = status

    def set_book_type(self, book_type):
        self.book_type = book_type

    def set_book_id(self, book_id):
        self.book_id = book_id

    def set_book_year(self, new_year):
        self.book_year = new_year


    #getting numbers

    def generate_book_id(self):
        if not self.book_id:
            counter = 0
            with open("books.json", "r") as file:
                line = file.readlines()
                if self.check_book_log_exists():
                    while line:
                        counter = + 1
                        line = file.readlines()
                    return counter
                else:
                    return 0
        else:
            return self.book_id


    #logging everything

    def add_book_to_library_stock(self):
        with open("books.json", "a+") as file:
            if not self.no_double_books():
                log_entry = {"book_id" : self.book_id, "name" : self.name, "author" : self.author, "year" : self.year,
                             "type" : self.book_type, "status" : self.loaned}
                file.write(json.dumps(',' +log_entry))
            else:
                raise DoubleBookIdError(f"Book with id {str(self.book_id)} already exists")

    def no_double_books(self):
        with open("books.json", "r") as file:
            line = file.readlines()
            while line:
                if json.loads(line[0])["book_id"] == self.book_id:
                    raise DoubleBookIdError(f"Book with id {str(self.book_id)} already exists")
                else:
                    line = file.readlines()
        file.close()

    @staticmethod
    def check_book_log_exists():
        books_file = 'books.json'
        with open(books_file, 'r') as file:
            line = file.readlines()
            if line:
                return True
            else:
                return False

def generate_book_id_manual():
        counter = 0
        with open("books.json", "r") as file:
            line = file.readlines()
            if Book.check_book_log_exists():
                while line:
                    counter = + 1
                    line = file.readlines()
                return counter
            else:
                return 0


# book3 = Book(book_id=10, name='The Hitchhikers Guide to the Galaxy', author='Douglas Adams', year=1980, book_type=1)
# book3.add_book_to_library_stock()


