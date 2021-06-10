class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name.title()
        self.type = cuisine_type.title()
    def describe_restaurant(self):
        print("Restaurant's name is " + self.name + ".")
        print("Restaurant's type is " + self.type + ".")
    def open_restaurant(self):
        print(self.name + " is opening.")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,favorate):
        super().__init__(restaurant_name,cuisine_type)
        self.favorate = favorate
    def display(self):
        print(self.favorate)