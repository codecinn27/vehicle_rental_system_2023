#Topic: Vehicle Rental System

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
    def __init__(self, brand, model, year, mileage, rental_price, plate_number,doors, seats):
        super().__init__(brand, model, year, mileage, rental_price, plate_number)
        self.doors = doors
        self.seats = seats

    def get_seat_capacity(self):
        return self.seats

    
#2nd child class, inherits from Vehicle (parent class)
class Bike(Vehicle):
    
    def __init__(self, brand, model, year, mileage, rental_price, plate_number, wheel_size):
        super().__init__(brand, model, year, mileage, rental_price, plate_number)
        self.wheel_size = wheel_size
    

# class to manage the vehicle rental system
class VehicleRentalSystem:

    #this class use dictionary to store the information of the vehicles
    def __init__(self):
        self.vehicle_dict = {}

    #add the vehicle information, key as the unique_id and all the vehicle information store as value
    #the class bike or car is store as value
    def add_vehicle(self, unique_id, vehicle):
        self.vehicle_dict[unique_id] = vehicle
        print("Vehicle added successfully.")

    #print all the document store inside the dictionary create when calling function add_vehicle
    def show_list(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            print("-------------------")
            print("Unique ID:", unique_id)
            print("Vehicle Details:")
            print("Brand:", vehicle.brand)
            print("Model:", vehicle.model)
            print("Year:", vehicle.year)
            print("Mileage:", vehicle.mileage)
            print("Rental Price:", vehicle.rental_price)
            print("--------------------")
    
    #print all the car list
    def show_list_car(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle, Car):
                print("-------------------")
                print("Unique ID:", unique_id)
                print("Vehicle Details:")
                print("Brand:", vehicle.brand)
                print("Model:", vehicle.model)
                print("Year:", vehicle.year)
                print("Mileage:", vehicle.mileage)
                print("Rental Price:", vehicle.rental_price)
                print("Door:", vehicle.doors)
                print("Seat:", vehicle.seats)
                print("--------------------")

    #print all the bike list
    def show_list_bike(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle, Bike):
                print("-------------------")
                print("Unique ID:", unique_id)
                print("Vehicle Details:")
                print("Brand:", vehicle.brand)
                print("Model:", vehicle.model)
                print("Year:", vehicle.year)
                print("Mileage:", vehicle.mileage)
                print("Rental Price:", vehicle.rental_price)
                print("Wheel Size:", vehicle.wheel_size)
                print("--------------------")
        
#example of the system
system = VehicleRentalSystem()

#storing information
#using list of tuples
vehicle_list = [
    (Car("Perodua", "Myvi", 2019, 20000, 100, "WUL7038",4,5), "P0001"),
    (Car("Proton", "Saga", 2011, 45000, 80, "VAP2302",4,5), "P0002"),
    (Car("Proton", "Persona", 2020, 10000, 120, "MAP311",4,5), "P0003"),
    (Car("Proton", "X50", 2021, 9000, 150, "VPP1132",4,7), "P0004"),
    (Bike("Yamaha", "LC135", 2017, 23000, 50, "WA2310P",27.5), "M0001"),
    (Bike("Yamaha", "Y15", 2019, 25000, 60, "PA2310P",29), "M0002"),
    (Bike("Honda", "RS150", 2020, 40000, 55, "JA2034P",29), "M0003"),
    (Bike("Honda", "EX5", 2016, 50000, 45, "MUP3043",27.5), "M0004")
]

#for loop and a list of tuples, you can conveniently add multiple vehicles into VehicleRentalSystem 
# without having to repeat the add_vehicle calls for each vehicle individually.
for vehicle, unique_id in vehicle_list:
    system.add_vehicle(unique_id, vehicle)

#print out all the added document to confirm whether the code works or not
# system.show_list_car()







    