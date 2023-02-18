# noinspection PyUnreachableCode
class Address:

    def __init__(self, city: str, street: str, house_num: int, po_num:int = None):
        self.city = city
        self.street = street
        self.house_num = house_num
        self.po_num: "str(int)" = po_num

    def __str__(self):
        if self.po_num is None:
            return f"city: {self.city}, street: {self.street}, house number: {self.house_num}"
        else:
            return f"city: {self.city}, street: {self.street}, house number: {self.house_num}, po box number: {self.po_num}"

    def __repr__(self):
        if self.po_num is None:
            return f"city: {self.city}, street: {self.street}, house number: {self.house_num}"
        else:
            return f"city: {self.city}, street: {self.street}, house number: {self.house_num}, po box number: {self.po_num}"

    #getters
    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_house_num(self):
        return self.house_num

    def get_po_num(self):
        return self.po_num

    #setters

    def set_house_num(self, new_house_num):
        self.house_num = new_house_num

    def set_street(self, new_street):
        self.street = new_street

    def set_city(self, new_city):
        self.city = new_city

    def set_po_num(self, new_po_num):
        self.po_num = new_po_num

# address = Address("raanana", "hamachtarot", 20, 4464624)

# print(address.__str__())
