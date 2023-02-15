import json
class LogError(Exception):
    pass
class LogNotFoundError(LogError):
    pass





class Log:
    def __init__(self, log_file='log.json'):
        self.log_file = log_file


    def write_log(self, log_entry):
        entry_num = self.get_entry_num()
        log_entry = {'entry_num': entry_num, **log_entry}
        with open(self.log_file, 'a+') as file:
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

log_file='log.json'
def check_for_lines_with(book_id):
    with open(log_file, 'r') as file:
        curr_line = file.readlines()
        if not curr_line:
            raise LogNotFoundError




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

    #for a centralized dump of all actions
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




