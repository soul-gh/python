cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
car='Audi'
if car=='audi':
    print("true")
if car.lower() == 'audi':
    print("true")
age_0=22
age_1=18
if age_0>=21 and age_1>=17:
    print("true")
if age_0>22 or age_1>19:
    print("true")
else:
    print("false")
requested_toppings=['mushroom','onions','pineapple']
if 'mushroom' in requested_toppings:
    print("T")
if 'pepperoni' not in requested_toppings:
    print("F")
age= 17
if age >=18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
if age<4:
    print("You admission cost is $0.")
elif age<18:
    print("You admission cost is $5.")
else:
    print("You admission cost is $10.")
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("You admission cost is $"+str(price)+".\n")

available_toppings=['mushrooms','green peppers','extra cheese','olives','pepperoni','pineapple']
requested_toppings=['mushrooms','green peppers','extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping=='green peppers':
                print("Sorry,we are out of green peppers right now.")
        else:
                print("Adding "+requested_topping+".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a pizza?")

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry, we don't have "+requested_topping+'.')
print("Finished making your pizza!")