class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name.title()
        self.type = cuisine_type.title()
        self.number_served = 0
    def update_number(self,number):
        self.number_served = number
    def increment_number(self,number):
        self.number_served += number
    def describe_restaurant(self):
        print("Restaurant's name is " + self.name + ".")
        print("Restaurant's type is " + self.type + ".")
    def open_restaurant(self):
        print(self.name + " is opening.")

restaurant1 = Restaurant('KFC','fast')
print("There were " + str(restaurant1.number_served) + " people came today.")
restaurant1.update_number(100)
print("There were " + str(restaurant1.number_served) + " people came today.")
restaurant1.increment_number(20)
print("There were " + str(restaurant1.number_served) + " people came today.")
print("\n")

class User():
    def __init__(self,first_name,last_name,age):
        self.name = first_name.title() + " " + last_name.title()
        self.age = age
        self.login_attempts = 1
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def describe_user(self):
        print("User's name is " + self.name + ".")
        print("User is " + str(self.age) + "year's old.")
    def greet_user(self):
        print("Hello," + self.name + "!")
user1 = User('monkey','luffy',19)
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
