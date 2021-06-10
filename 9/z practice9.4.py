from restaurant import Restaurant
my_restaurant = Restaurant('KFC','chicken')
my_restaurant.describe_restaurant()

import user
privileges = ('edit web','change name')
admin = user.Admin('kaku','kou',26,privileges)
admin.privileges.show_privileges()


