import address
import dates

class Customer:

    def __init__(self, id: int, name: str, address: address.Address, email, birthday):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.birthday = birthday

#maybe address is completely useless, no need to complicate something for no reason
        # address - diffrent class to confirm all details correct
        #birthday - diffrent class to work with datetime module

def nothing():
    print("hi")