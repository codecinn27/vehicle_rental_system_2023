#Topic: Vehicle Rental System
from data_list import vehicle_list
from vehicle_rental_system import Car, Bike

#use the sys module to call the exit() function
import sys
# class to manage the vehicle rental system
class VehicleRentalSystem:

    #this class use dictionary to store the information of the vehicles
    def __init__(self):
        self.vehicle_dict = {}

    #add the vehicle information, key as the unique_id and all the vehicle information store as value
    #the class bike or car is store as value
    def add_vehicle(self, unique_id, vehicle):
        self.vehicle_dict[unique_id] = vehicle
        #uncomment to test the code's functionality after adding it
        # print("Vehicle added successfully.")

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

    
    #delete vehicle from the list
    def remove_vehicle(self, id):
        if id in self.vehicle_dict:
            del self.vehicle_dict[id]
            print(f"Vehicle with unique ID '{id}' has been removed.")
        else:
            print(f"Vehicle with unique ID '{id}' does not exist in the rental system.")

    
    def reserve_vehicle(self, unique_id):
        if unique_id in self.vehicle_dict:
            vehicle = self.vehicle_dict[unique_id]
        
    #def return  vehicle
    #def calculate_rental_cost
#example of the system

def print_menu():
    print("Welcome to the Vehicle Rental System!")
    print("1. Show List of Bikes")
    print("2. Rent a Bike")
    print("3. Show List of Cars")
    print("4. Rent a Car")
    print("5. Show List of All Vehicles")
    print("6. Exit")

# def rent_bike(system):  
#def rent_car(system):


def main():
    #call out system and store it as a object
    system = VehicleRentalSystem()
    from data_list import vehicle_list
    #for loop and a list of tuples, you can conveniently add multiple vehicles into VehicleRentalSystem 
    # without having to repeat the add_vehicle calls for each vehicle individually.
    for vehicle, unique_id in vehicle_list:
        system.add_vehicle(unique_id, vehicle)

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        # Use a dictionary to map the choice to the corresponding function
        #without lambda expression these functions will be called immediately when the menu_options dictionary is defined
        # rather than being called when the user selects the corresponding menu option
        #therefore, wrap the function calls in lambda functions
        #This will delay the execution of the functions until they are called later on.
        menu_options = {
            #print out all the bike that store in the dictionary
            "1": lambda : system.show_list_bike(),
            #print out all the car that store in the dictionary
            "3": lambda : system.show_list_car(),
            #print out all the added document 
            "5": lambda : system.show_list(),
            "6": lambda : sys.exit(0)
        }

        if choice in menu_options:
            print("\n")
            #call out the function based on user input 
            menu_options[choice]()
        else:
            print("Invalid input, please try again\n")
    

main()