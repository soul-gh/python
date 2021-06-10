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