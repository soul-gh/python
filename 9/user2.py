from user1 import User
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

privileges = ('edit web','change name')
admin = Admin('kaku','kou',26,privileges)
admin.privileges.show_privileges()
