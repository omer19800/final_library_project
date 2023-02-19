import json

class LogError(Exception):
    pass
class LogNotFoundError(LogError):
    pass

log_file = 'log.json'

class Log:
    def __init__(self, log_file='log.json'):
        self.log_file = log_file #  # no


def write_log(log_entry):
    entry_num = get_entry_num()
    log_entry = {'entry_num': entry_num, **log_entry}
    with open(log_file, 'a+') as file:
        file.write(json.dumps(log_entry) + '\n')

def get_entry_num(self):
    try:
        with open(self.log_file, 'r') as file:
            lines = file.readlines()
            if not lines:
                return 0
            else:
                latest_entry = json.loads(lines[-1])
                return latest_entry['entry_num'] + 1
    except FileNotFoundError:
        return 0


#make sure each log file exists
def check_log_exists():
    with open(log_file, 'r') as file:
        line = file.readlines()
        return bool(line)


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



#getting certain log entries
# def check_for_logs_of_book(book_id):
#     relevant_logs = []
#     try:
#         with open(log_file, 'r') as file:
#             line_list = file.readlines()
#             if check_book_log_exists() is True:
#                 for line in line_list:
#                     curr_log_line = json.loads(line.strip('\n'))  # recieves a list
#                     if curr_log_line["book_id"] == book_id:
#                         relevant_logs.append(curr_log_line)
#                     elif curr_log_line["book_id"] != book_id:
#                         pass
#                 return relevant_logs
#             else:
#                 raise LogNotFoundError
#     except LogNotFoundError:
#         print("Error - Log Not Found - Log file is missing or there was a problem with the logs themselves")

def get_book_object_by_id(book_id):
    book_details = []
    import book
    try:
        with open("books.json", "r") as file:
            line_list = file.readlines()
            if check_book_log_exists() is True:
                for line in line_list:
                    curr_log_line = json.loads(line.strip('\n')) #recieves a list
                    if curr_log_line["book_id"] == book_id:
                        book_details.append(curr_log_line)
                    elif curr_log_line["book_id"] != book_id:
                        pass
        book_obj = book.Book(book_id, book_details[0]["name"], book_details[0]["author"], int(book_details[0]["year"]))
        book_obj.set_book_type = book_obj.get_type()
        book_obj.set_book_id = book_obj.generate_book_id()

        return book_obj

    except Exception:
        LogNotFoundError("error, log with book id was not found")
def check_for_customer_details(customer_id):
    relevant_line = []
    customers_file = 'customers.json'
    try:
        with open(customers_file , 'r') as file:
            line = file.readlines()
            if check_log_exists():
                while line:
                    curr_log_line = json.loads(line)
                    if curr_log_line["customer_id"] == customer_id:
                        relevant_line.append(curr_log_line)
                    else:
                        line = file.readline()
                return relevant_line
            else:
                raise LogNotFoundError
    except LogNotFoundError:
        print("Error - Log Not Found - Log file is missing or there was a problem with the logs themselves")



check_for_logs_of_book(10)








