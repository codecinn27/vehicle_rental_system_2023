#Topic: Vehicle Rental System
from data_type import Car, Bike

#use the sys module to call the exit() function
import sys
# class to manage the vehicle rental system
class VehicleRentalSystem:

    #this class use dictionary to store the information of the vehicles
    def __init__(self):
        self.vehicle_dict = {}

    #add the vehicle information, key as the unique_id and all the vehicle information store as value
    #the class bike or car is store as value
    def add_vehicle(self, vehicle,unique_id):
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
                vehicle.print_info()
                print("Unique ID:", unique_id)
                print("--------------------")

    #print all the bike list
    def show_list_bike(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle, Bike):
                vehicle.print_info()
                print("Unique ID:", unique_id)
                print("-------------------")
    
    #store vechicle into separete dictionary based on its type
    def get_vehicle_list(self, type):
        #create a temporary dictionary first, so that later can return this list
        vehicle_list = {}
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle,type):
                vehicle_list[unique_id] = vehicle
        return vehicle_list


    #delete vehicle from the list
    def remove_vehicle(self, id):
        if id in self.vehicle_dict:
            del self.vehicle_dict[id]
            print(f"Vehicle with unique ID '{id}' has been removed.")
        else:
            print(f"Vehicle with unique ID '{id}' does not exist in the rental system.")

    def reserve_vehicle(self, id):
        if id in self.vehicle_dict:
            vehicle = self.vehicle_dict[id]
            if vehicle.get_availability():
                #if vehicle is available then, reserve the vehicle
                vehicle.set_availability(False)
                print(f"Vehicle with unique ID '{id}' has been reserved.")
            else:
                print(f"Vehicle with unique ID '{id}' is not available for reservation.")
        else:
            print(f"Vehicle with unique ID '{id}' does not exist in the rental system.")

    #rent a bike
    def rent_bike(system):
        bike_list = system.get_vehicle_list(Bike)
        print("Bike List:")
        for id, vehicle in bike_list.items():
            if vehicle.get_availability():
                print("-------------------")
                print("Unique ID:", id)
                print("Vehicle Details:")
                print("Brand:", vehicle.brand)
                print("Model:", vehicle.model)
                print("Year:", vehicle.year)
                print("Mileage:", vehicle.mileage)
                print("Rental Price:", vehicle.rental_price)
                print("Wheel Size:",vehicle.wheel_size)
                print("--------------------")
        bike_id = input("Enter the unique ID of the bike you want to rent (or 0 to go back): ")
        if bike_id == "0":
            return
        system.reserve_vehicle(bike_id)
        print("Bike rented successfully!")
        
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
        system.add_vehicle(vehicle,unique_id)

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
            #rent a bike
            "2": lambda : system.rent_bike(),
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