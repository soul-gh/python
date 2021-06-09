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
favorate = ['strawberry','banana','orange']
my_icestand = IceCreamStand('bobo','ice',favorate)
my_icestand.display()

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

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age,privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)
privileges = ['can add post','can delete post','can ban user']
admin = Admin('roronoa','zoro',20,privileges)
admin.privileges.show_privileges()