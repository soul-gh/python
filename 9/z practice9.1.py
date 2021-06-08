class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name.title()
        self.type = cuisine_type.title()
    def describe_restaurant(self):
        print("Restaurant's name is " + self.name + ".")
        print("Restaurant's type is " + self.type + ".")
    def open_restaurant(self):
        print(self.name + " is opening.")
restaurant1 = Restaurant('KFC','fast')    
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('M','fast')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('huangmenji','chicken')
restaurant3.describe_restaurant()

class User():
    def __init__(self,first_name,last_name,age):
        self.name = first_name.title() + " " + last_name.title()
        self.age = age
    def describe_user(self):
        print("User's name is " + self.name + ".")
        print("User is " + str(self.age) + "year's old.")
    def greet_user(self):
        print("Hello," + self.name + "!")
user1 = User('monkey','luffy',19)
user1.describe_user()
user1.greet_user()