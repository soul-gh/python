class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer.")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def get_descriptie_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptie_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()