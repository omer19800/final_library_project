class Address:

    def __init__(self, city: str, street: str, house_num: int):
        self.city = city
        self.street = street
        self.house_num = house_num
        self.po_num = str(int)

    def get_house_num(self):
        return self.house_num

    def set_house_num(self, new_house_num):
        self.house_num = new_house_num

    def get_street(self):
        return self.street

    def set_street(self, new_street):
        self.street = new_street

    def get_city(self):
        return self.city

    def set_city(self, new_city):
        self.city = new_city

    def get_po_num(self):
        return self.po_num

    def set_po_num(self, new_po_num):
        self.po_num = new_po_num


