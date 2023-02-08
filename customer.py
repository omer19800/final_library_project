import address
import dates
import re
import random
import json
class CustomerError(Exception):
    pass
class EmailError(CustomerError):
    pass


class Customer:

    def __init__(self, id: int, name: str, email:str, birthday:str, city, street, house_num, po_num=None):
        self.id = id
        self.name = name
        self.address = address.Address(city, street, house_num, po_num)
        self.email = check_email(email)
        self.birthday = birthday #just require format dd-mm-yyyy
        self.customer_id = random.randint(1, 10000)
        self.loaned_books = []

    def __repr__(self):
        pass
    #getters
    def get_customer_personal_id(self):
        return self.id

    def get_customer_name(self):
        return self.name

    def get_customer_address(self):
        return address.str

    def get_customer_email(self):
        return self.email

    def get_customer_birthday(self):
        return self.birthday

    def get_customer_loaned_books(self):
        return self.loaned_books

    #setters
    def set_customer_name(self, new_name):
        self.customer_name = new_name

    def set_customer_birthday(self, new_birthday):
        self.birthday = new_birthday

    def set_customer_customer_id(self, new_id):
        self.customer_id = new_id
    def set_customer_loans(self, the_list:list):
        self.loaned_books = the_list

    def add_loaned_book_to_customer(self, new_book_id):
        self.loaned_books.append(new_book_id)

    def remove_loaned_book_from_customer(self, book_id):
        self.loaned_books.pop(book_id)

    def set_customer_id(self, id):
        self.customer_id = id

    def set_customer_email(self, new_email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #thanks internet
        if (re.search(regex, new_email)):
            self.email = new_email
        else:
            self.email = None
            raise EmailError("Invalid Email")
    def set_new_customer_address(self, city, street, house_num, po_num=None):
        self.address = address.Address(city, street, house_num)
        self.address.po_num = po_num


    def generate_customer_id(self): #chat
        while True:
            customer_id = str(random.randint(10000, 999999))
            if not self.check_customer_id(customer_id):
                return customer_id

    def check_customer_id(self, customer_id): #chat
        with open('customers.json', 'r') as f:
            customers = json.load(f)
        for customer in customers:
            if customer['customer_id'] == customer_id:
                return True
        return False

    @staticmethod
    def get_customer_details_by_name(name): #chat
        with open('customers.json', 'r') as f:
            customers = json.load(f)
        result = []
        for customer in customers:
            if customer['name'] == name:
                result.append(customer)
        return result

    # @staticmethod
    # def get_customer_details_by_id(customer_id): #chat
    #     with open('customers.json', 'r') as f:
    #         customers = json.load(f)
    #     for customer in customers:
    #         if customer['customer_id'] == customer_id:
    #             return customer
    #     return None



    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'id': self.id,
            'name': self.name,
            'address': self.address.__repr__(),
            'email': self.email,
            'birthday': self.birthday,
            'curr_loaned': self.loaned_books
        }

    def add_to_customer_file(self):
        with open('customers.json', 'a') as f:
            json.dump((',' + self.to_dict()), f)


def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #thanks internet
    return email if re.search(regex, email) else None


#
# customer = Customer(id=2, name="Omer Eshel",email="omer198000@gmail.com", birthday="19-08-2000", city="Kefar Saba",
#                     street="Yaair Rozenblum", house_num="12345")

# print(customer.address.city)
# customer.add_to_customer_file()

