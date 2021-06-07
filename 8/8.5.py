def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print('-' + topping)
make_pizza('pepperoni')
make_pizza('mushroom','peppers')

def make_pizza(size,*toppings):
    print("Making a "+ str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('-' + topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','peppers','cheese')
print("\n")

#关键字实参
def build_profile(first, last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)


