# https://certifysphere.com/docs/tutorials/learn-python/object-oriented-programming


#https://certifysphere.com/docs/tutorials/learn-python/object-oriented-programming#classes-and-objects
# Class definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car has stopped.")

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

#Class Definition End

# Creating objects
car1 = Car("Ford", "Mustang", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accessing attributes and calling methods
print(car1.make)  # Output: Ford
print(car1.model)  # Output: Mustang
print(car1.year)  # Output: 2022
car2.display_info()  # Output: Car: Tesla Model S, Year: 2023

# Run this program in terminal or command : 
# python3 car.py or python car.py

###################
# https://certifysphere.com/docs/tutorials/learn-python/object-oriented-programming#inheritance-and-polymorphism
#####################
# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("The electric car is charging.")

# Creating objects of ElectricCar
my_car = ElectricCar("Tesla", "Model S", 2023, "100kWh")
my_car.charge() # Output The electric car is charging.
# Run this program in terminal or command : 
# python3 car.py or python car.py

