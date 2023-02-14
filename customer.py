import address
import dates

class Customer:

    def __init__(self, id: int, name: str, address: address.Address(city=city,street=street,house_num=house_num), email, birthday):
        self.id = id
        self.name = name
        self.address = Address(city, street, housenum)
        self.email = email
        self.birthday = birthday

#maybe address is completely useless, no need to complicate something for no reason
        # address - diffrent class to confirm all details correct
        #birthday - diffrent class to work with datetime module

    #getters
    def get_customer_id(self):
        return self.id

    def get_customer_name(self):
        return self.name

    def get_customer_address:
        return address.str

