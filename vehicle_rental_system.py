#parent class
class Vehicle:

    # __init__ is a python constructor
    # is used to assign value to the attributes of the object
    def __init__(self, brand, model, year, mileage, rental_price, plate_number):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.rental_price = rental_price
        self.plate_number = plate_number
    
    def set_availabilty(self, availability):
        self.availability = availability

    def get_availability(self):
        return self.availability

#1st child class, inherits from Vehicle (parent class)
class Car(Vehicle):

    #use super().__init__ is a python constructor 
    #It allows the child class to inherit and initialize the attributes and behavior defined in the parent classto initialize the attributes and behavior defined in the parent class
    def __init__(self, brand, model, year, mileage, rental_price, plate_number, doors, seats):
        super().__init__(brand, model, year, mileage, rental_price, plate_number)
        self.doors = doors
        self.seats = seats

    def get_seat_capacity(self):
        return self.seats

    
#2nd child class, inherits from Vehicle (parent class)
class Bike(Vehicle):
    
    def __init__(self, brand, model, year, mileage, rental_price, plate_number,wheel_size):
        super().__init__(brand, model, year, mileage, rental_price, plate_number)
        self.wheel_size = wheel_size
    











    