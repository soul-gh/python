def ordered_sandwich(*toppings):
    print("You ordered a sandwich with ")
    for topping in toppings:
        print("-" + topping)
ordered_sandwich('corn', 'chicken', 'salad')
ordered_sandwich('beef')

def build_profile(first, last,**user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('hao','guo',height = '180cm',location = 'tokyo',field = 'computer',)
print(user_profile)

def cars_info(maker, type, **info):
    car = {}
    car['maker'] = maker
    car['type'] = type
    for key,value in info.items():
        car[key] = value
    return car
car = cars_info('subaru', 'outback', color='blue',tow_package=True)
print(car)

import pizza as p
p.make_pizza(12,'mushrooms','green peppers','extra cheese')
from pizza import make_pizza as mp
mp(16,'mushrooms')
print("\n")

import pizza as p
p.make_pizza(16,'cheese')
