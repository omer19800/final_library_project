import address
import customer
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
        self.email = check_customer_email_with_value(email)
        self.birthday = check_birthday_with_value(birthday) #just require format dd-mm-yyyy
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
            "customer_id": self.customer_id,
            "id": self.id,
            "name": self.name,
            "address": self.address.__repr__(),
            "email": self.email,
            "birthday": self.birthday,
            "curr_loaned": self.loaned_books
        }

    def add_to_customer_file(self):
        # Load the existing data as a list of objects
        with open('customers.json', 'r') as f:
            customers = json.load(f)

        # Append the new customer object to the list
        customers.append(self.to_dict())

        # Convert the values to double quotes
        customers_json = str(customers).replace("'", '"')

        # Write the entire list of objects to the file as a valid JSON string
        with open('customers.json', 'w') as f:
            f.write(customers_json)

# def check_email(email):
#     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #thanks internet
#     return email if re.search(regex, email) else None

def check_customer_email_with_value(email): #for front end
    for i in range(2):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Invalid email address. Please try again.")
    print("Failed to provide valid email address after two attempts.")
    return None
def check_customer_email(): #for front end
    for i in range(2):
        email = input("Enter customer email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Invalid email address. Please try again.")
    print("Failed to provide valid email address after two attempts.")
    return None

def check_birthday(): #for frontend
    pattern = r'^([0-3][0-9])/([01][0-9])/([0-9]{2})$'
    for i in range(2):
        birthday = input("Please enter your birthday in the format dd/mm/yy: ")
        match = re.match(pattern, birthday)
        if match:
            return match.group(1) + '/' + match.group(2) + '/' + match.group(3)
        print("Invalid input. Please try again.")
    print("Max attempts reached. Setting birthday to None.")
    return None

def check_birthday_with_value(birthday): #for frontend
    pattern = r'^([0-3][0-9])/([01][0-9])/([0-9]{2})$'
    for i in range(2):
        match = re.match(pattern, birthday)
        if match:
            return match.group(1) + '/' + match.group(2) + '/' + match.group(3)
        print("Invalid input. Please try again.")
    print("Max attempts reached. Setting birthday to None.")
    return None

#
# customer = Customer(id=5, name="Pardonski Damzel",email="shawrma56@gmail.com", birthday="12/13/12", city="Kefar Saba",
#                     street="kebab", house_num="12")



# customer.add_to_customer_file()