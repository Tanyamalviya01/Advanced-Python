class Customer: # customer class
    def __init__(self, id, name, address, email, phone, member):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member = member
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_member(self):
        return self.member

class Transaction: # transaction class
    def __init__(self, date, item, cost, id):
        self.date = date
        self.item = item
        self.cost = cost
        self.id = id
    
    def get_date(self):
        return self.date
    
    def get_item(self):
        return self.item
    
    def get_cost(self):
        return self.cost
    
    def get_id(self):
        return self.id
