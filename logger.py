import json


class LogError(Exception):
    pass


class LogNotFoundError(LogError):
    pass


class Log:
    def __init__(self, log_file='log.json'):
        self.log_file = log_file

    def write_log(self, log_entry):
        # entry_num = self.get_entry_num()
        # log_entry = {'entry_num': entry_num, **log_entry}
        with open(self.log_file, 'a+') as file:
            file.write(json.dumps(log_entry) + '\n')

    # def get_entry_num(self):
    #     try:
    #         with open(self.log_file, 'r') as file:
    #             lines = file.readlines()
    #             if not lines:
    #                 return 0
    #             else:
    #                 latest_entry = json.loads(lines[-1])
    #                 return latest_entry['entry_num'] + 1
    #     except FileNotFoundError:
    #         return 0


def check_for_lines_with(book_id):
    log_file = 'log.json'
    relevant_logs = []
    try:
        with open(log_file, 'r') as file:
            line = file.readlines()
            if check_log_exists():
                while line:
                    curr_log_line = json.loads(line)
                    if curr_log_line["book_id"] == book_id:
                        relevant_logs.append(curr_log_line)
                        line = file.readline()
                    else:
                        line = file.readline()
                return relevant_logs
            else:
                raise LogNotFoundError
    except LogNotFoundError:
        print("Error - Log Not Found - Log file is missing or there was a problem with the logs themselves")


def check_log_exists():
    log_file = 'log.json'
    with open(log_file, 'r') as file:
        line = file.readlines()
        if not line:
            return False
        else:
            return True

def check_book_log_exists():
    books_file = 'books.json'
    with open(books_file, 'r') as file:
        line = file.readlines()
        if not line:
            return False
        else:
            return True





# def read_logs(self) -> list:
#     with open(self.log_file, 'r') as file:
#         line = file.readline()
#         logs = []
#         while line:
#             log = json.loads(line)
#             logs.append(log)
#             line = file.readline()
#     return logs


log = Log()

# def search_log_by_book_id(self, book_id):
#     with open(self.log_file, 'r') as file:
#         line = file.readline()
# logs = []
# while line:
#     log = json.loads(line)
# if log['book_id'] == book_id:
#     logs.append(log)
# line = file.readline()
# raise LogNotFoundError("Log with book ID {} not found.".format(book_id))

# for a centralized dump of all actions
#  try:
#         with open('logs.json', 'r') as file:
#             contents = json.load(file)
#             highest_entry_num = max([log['entry_num'] for log in contents])
#     except FileNotFoundError:
#         highest_entry_num = 0
#
#     with open('logs.json', 'a') as file:
#         for log_entry in self.log_entries:
#             highest_entry_num += 1
#             log_entry['entry_num'] = highest_entry_num
#             file.write(json.dumps(log_entry))
#             file.write('\n')
