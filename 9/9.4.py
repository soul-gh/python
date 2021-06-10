from car import Car
my_new_car = Car('audi','a8','2021')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from car import ElectricCar
my_tesla = ElectricCar('tesla','model s',2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

import car
my_beetle = car.Car('volkswagen','beetle',2021)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla','roadster',2021)
print(my_tesla.get_descriptive_name())