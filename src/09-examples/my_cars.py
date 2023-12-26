# Import specific classes of a module.
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("-- end of the first example\n")

# Import an entire module.
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("-- end of the second example\n")

# Import a module into a module
from car_final import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("-- end of the third example\n")

# Using Aliases.
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())