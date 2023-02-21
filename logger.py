import json

import Levenshtein as Levenshtein

import dates
import customer
import book
from fuzzywuzzy import fuzz
import Levenshtein

class LogError(Exception):
    pass
class LogNotFoundError(LogError):
    pass
class CustomerHasActiveLoans(Exception):
    pass
class BookNotFoundError(LogError):
    pass


log_file = 'log.json'

class Log:
    def __init__(self, log_file='log.json'):
        self.log_file = log_file # no


def get_entry_num():
    counter = 0
    try:
        with open(log_file, 'r') as file:
            lines = file.read()
            if not lines:
                return 0
            data = json.loads(lines)
            for entry in data:
                counter += 1
            return counter + 1
    except FileNotFoundError:
        return 0

# latest_entry = json.loads(lines[-1])
                # return latest_entry[-1]['entry_num'] + 1

def write_log(log_entry):
    with open(log_file, "r") as file:
        data:list = json.load(file)
    entry_num = get_entry_num()
    log_entry = {'entry_num': entry_num, **log_entry}
    data.append(log_entry)
    with open(log_file, "w") as file:
        json.dump(data, file)


#make sure each log file exists
def check_log_exists():
    with open(log_file, 'r') as file:
        line = file.readlines()
        if line:
            return True
        else:
            return False

def check_book_log_exists():
    books_file = 'books.json'
    with open(books_file, 'r') as file:
        line = file.readlines()
        if line:
            return True
        else:
            return False

def check_customers_log_exists():
    customer_file = 'customers.json'
    with open(customer_file, 'r') as file:
        line = file.readlines()
        return bool(line)



# getting certain log entries
def get_last_loaner_id(book_id):
    try:
        with open(log_file, 'r') as file:
            if check_book_log_exists():
                logs = json.load(file)
                for curr_log in reversed(logs):
                    if curr_log["book_id"] == book_id and curr_log["type"] == "loan":
                        return curr_log["customer_id"]
            else:
                raise LogNotFoundError(
                    "Error - Log Not Found - Log file is missing or there was a problem with the logs themselves")
    except LogNotFoundError as e:
        print(e)
        

# getting book and loan instances and customer  from the id`s to interact with in the library file
def get_book_object_by_id(book_id):
    book_details = []
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            for curr_book in books:
                if curr_book["book_id"] == book_id:
                    book_details.append(curr_book)
                    break

            if len(book_details) == 0:
                raise LogNotFoundError

        book_obj = book.Book(book_id, book_details[0]["name"], book_details[0]["author"], int(book_details[0]["year"]))
        book_obj.set_book_type(int(book_details[0]["type"]))
        book_obj.set_loaned_or_not(book_details[0]["status"])
        book_obj.set_book_id(book_id)
        return book_obj

    except Exception:
        raise LogNotFoundError("error, log with book id was not found")

#
def getting_loan_instance_by_id(selected_book, book_id, customer_id):
    import loan
    log_details = []
    try:
        with open("log.json", "r") as file:
            if check_log_exists():
                logs = json.load(file)
                for curr_log in reversed(logs):
                    if curr_log["book_id"] == book_id and curr_log["type"] == "loan":
                        log_details.append(curr_log)
                    break

            else:
                raise LogNotFoundError("error, log file was not found or there was an error")

        loan_instance = loan.Loan(selected_book, book_id, customer_id)
        loan_instance.set_loan_date(curr_log["loan_date"])
        loan_instance.set_return_date(curr_log["return_date"])
        return loan_instance

    except LogNotFoundError:
        print("Error - Log Not Found - Log file is missing or there was a problem with the logs")

#chat
def get_customer_instance_by_id(customer_id):
    from customer import Customer

    try:
        with open("customers.json", "r") as file:
            customers = json.load(file)
    except FileNotFoundError:
        print("customers.json file not found!")
        return None

    for person in customers:
        if person["customer_id"] == customer_id:
            # Split address string into parts
            address_parts = person["address"].split(", ")
            city = address_parts[0].split(": ")[1]
            street = address_parts[1].split(": ")[1]
            house_num = address_parts[2].split(": ")[1]

            # Create and return Customer instance
            selected_customer = Customer(
                id=id,
                name=person["name"],
                email=person["email"],
                birthday=person["birthday"],
                city=city,
                street=street,
                house_num=house_num)
            selected_customer.set_customer_loans(person["curr_loaned"])
            selected_customer.set_customer_customer_id(customer_id)

            return selected_customer


    print(f"Customer with id {customer_id} not found in logs!")
    return None

#chat
def get_all_customers_details():
    with open("customers.json", "r") as f:
        customers = json.load(f)
        for customer in customers:
            print("Customer ID:", customer["customer_id"])
            print("Name:", customer["name"])
            print("Address:", customer["address"])
            print("Email:", customer["email"])
            print("Birthday:", customer["birthday"])
            print("Current Loaned Books:", customer["curr_loaned"])
            print("----------------------------------------------------------------")

def get_customer_details_by_id(customer_id):
    with open("customers.json", "r") as f:
        customers = json.load(f)
        for customer in customers:
            if customer["customer_id"] == customer_id:
                print("----------------------------------------------------------------")
                print("Customer ID:", customer["customer_id"])
                print("Name:", customer["name"])
                print("Address:", customer["address"])
                print("Email:", customer["email"])
                print("Birthday:", customer["birthday"])
                print("Current Loaned Books:", customer["curr_loaned"])
                print("----------------------------------------------------------------")


#updates

#chat
def update_book_status(book_id, new_status):
    if check_book_log_exists():
        try:
            with open("books.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            print("books.json file not found!")
            return

            # Find the book with the given book_id and update its status
        found_book = False
        for book in books:
            if book["book_id"] == book_id:
                book["status"] = new_status
                found_book = True
                break

        if not found_book:
            print(f"Book with id {book_id} not found in logs!")
            return

        # Rewrite the books.json file with updated data
        with open("books.json", "w") as file:
            json.dump(books, file)

    else:
        raise LogNotFoundError("Book with id {book_id} not found")




#chat
def update_a_customer_instance(changed_customer_instance):
    with open('customers.json', 'r') as f:
        customers = json.load(f)

    for i, c in enumerate(customers):
        if c['customer_id'] == changed_customer_instance.customer_id:
            customers[i] = changed_customer_instance.to_dict()

    with open('customers.json', 'w') as f:
        for c in customers:
            json.dump(c, f)

def update_a_customer_loans(customer_id, book_id):
    with open('customers.json', 'r') as f:
        customers = json.load(f)

    for i, c in enumerate(customers):
        if c['customer_id'] == customer_id:
            c['curr_loaned'].append(book_id)
            customers[i] = c

    with open('customers.json', 'w') as f:
        json.dump(customers, f,)

def remove_book_from_customer(customer_id, book_id):
    with open('customers.json', 'r') as f:
        customers = json.load(f)

    for customer in customers:
        if customer['customer_id'] == customer_id:
            customer['curr_loaned'].remove(book_id)

    with open('customers.json', 'w') as f:
        json.dump(customers, f)

def remove_book(book_id):
    with open("books.json", "r") as file:
        data = json.loads(file.read())

    for book in data:
        if book["book_id"] == book_id:
            if book["status"] == "True":
                raise book.BookOnLoanError(f"Book with id {book_id} is on loan!")
            else:
                data.remove(book)
                break

    with open("books.json", "w") as file:
        json.dump(data, file)
#add book is inside book file



def remove_a_customer(customer_id): #based on the fact you technically return the library card when you leave it - allegedly
    try:
        with open('customers.json', 'r') as file:
            customers = json.load(file)
    except FileNotFoundError:
        print("Error: customers.json file not found.")
        return

        # find the customer with the given id
    customer_index = None
    for index, customer in enumerate(customers):
        if customer['customer_id'] == customer_id:
            customer_index = index
            break

    if customer_index is None:
        print(f"Error: Customer with ID {customer_id} not found.")
        return

    # check if the customer has any active loans
    if customers[customer_index]['curr_loaned']:
        raise CustomerHasActiveLoansError("Error: Cannot remove customer with active loans.")

    # remove the customer from the list
    del customers[customer_index]

    # write the updated list of customers back to the file
    with open('customers.json', 'w') as file:
        json.dump(customers, file)
    print(f"Customer with ID {customer_id} has been removed.")

#printing all logs #chat

def print_all_logs():
    with open("log.json", "r") as file:
        logs = json.load(file)
        print("----------------------------------------------------------------")
        for log in logs:
            print("Entry Num:", log["entry_num"])
            print("Entry Type:", log["type"])
            print("Book ID:", log["book_id"])
            print("Customer ID:", log["customer_id"])
            print("Loan Date:", log["loan_date"])
            print("Return Date", log["return_date"])
            if log["status"]:
                if log["status"] == "returned on time":
                    print("Status:", log["status"])
                elif log["status"] == "late":
                    print("Status:", log["status"])
                    print("Original Return Date:", log["original_return_date"])
                    print("How Late Was The Customer:", log["days_late"])
            else:
                print("Status:", log["status"])
            print("----------------------------------------------------------------")

    # chat

def print_all_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        print("books.json file not found!")
        return
    print("----------------------------------------------------------------")
    for book in books:

        print(f"Book ID: {book['book_id']}")
        print(f"Name: {book['name']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print(f"Type: {book['type']}")
        print(f"Status: {'available' if book['status'] else 'not available'}")
        print("----------------------------------------------------------------")

def print_all_late_logs():
    with open(log_file, 'r') as file:
        if check_book_log_exists():
            logs = json.load(file)
            print("----------------------------------------------------------------")
            for log in logs:
                if log["type"] == "return" and log["status"] == "late":
                    print("Log Entry Number:", log["entry_num"])
                    print("Log Entry Type:", log["type"])
                    print("Book ID:", log["book_id"])
                    print("Customer ID:", log["customer_id"])
                    print("Loan Date:", log["loan_date"])
                    print("Actual Return Date:", log["return_date"])
                    print("Original Return Date:", log["original_return_date"])
                    print("How Late Was The Customer:", log["days_late"])
                    print("Status:", log["status"])
                    print("----------------------------------------------------------------")

#yet again getting ids from strings
#found about about fuzzy wuzzy package that compares strings and outputs the best match ratio, so used that
#dont forget to install fuzzywuzzy package
def get_book_id_from_name(book_name:str):
    with open('books.json', 'r') as file:
        content = json.load(file)
        best_match = None
        best_ratio = 0
        for book in content:
            ratio = fuzz.token_set_ratio(book_name, book['name'])
            if ratio > best_ratio:
                best_match = book['book_id']
                best_ratio = ratio
        if best_match:
            return best_match
        else:
            raise BookNotFoundError("Book was not found")


def get_customer_id_from_name(customer_name):
    with open("customers.json", "r") as file: #chat
        content = json.load(file)
        for customer in content:
            name = customer["name"]
            score = fuzz.token_sort_ratio(name.lower(), customer_name.lower())
            if score >= 80:  # set a threshold for the score
                return customer["customer_id"]
    # return None if no match is found
    return None

def get_customer_loans(customer_id):
    def print_customer_loans(customer_id):
        with open('loans.json', 'r') as f:
            loans = json.load(f)

        if customer_id not in loans:
            print(f"No active loans found for customer {customer_id}")
        else:
            customer_loans = loans[customer_id]
            print(f"Active loans for customer {customer_id}:")
            for book_id, loan_info in customer_loans.items():
                print(f"Book {book_id}:")
                print(f"Title: {loan_info['book_title']}")
                print(f"Loaned on: {loan_info['loan_date']}")
                print(f"Expected return date: {loan_info['return_date']}")

def get_all_customers():
    try:
        with open("customers.json", "r") as file:
            customers = json.load(file)
    except FileNotFoundError:
        print("customers.json file not found!")
        return
        return

    print("----------------------------------------------------------------")
    for customer in customers:
        print(f"ID: {customer['id']}")
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print(f"Birthday: {customer['birthday']}")
        print(f"Address: {customer['address']}")
        print("----------------------------------------------------------------")


# write_log({"test,test,test" : "test,test,test"})
