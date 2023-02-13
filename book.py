class Book:

    def __init__(self, book_id: int, name: str, author: str, year: int, book_type: int) -> object:
        self.book_id = id
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
        if status:
            self.loaned = True
        elif not status:
            self.loaned = False
        else:
            pass

#types: 1 up to 10 days, 2 up to 5 days, 3 up to 2 days

