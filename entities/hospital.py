class Hospital:
    name:str
    address:str
    city:str
    state:str
    zipcode:str
    phone:str
    email:str
    website:str
    
    def __init__(self, name, address, city, state, zipcode, phone, email, website):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.email = email
        self.website = website