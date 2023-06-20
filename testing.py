from data_type import Car, Bike

car1 = Car("Perodua", "Myvi", 2019, 20000, 100, "WUL7038", 4, 5)
bike1 = Bike("Yamaha", "LC135", 2017, 23000, 50, "WA2310P", 27.5)
if car1.get_availability():
    print("Bike is available")