print("hello git world!\n")
tianxian_baobao=["dingding","dixi","lala","po"]
for namelist in tianxian_baobao:
    print(namelist)
print(namelist)
for namelist in tianxian_baobao:
    print("I like "+namelist.title())
    print("I can't wait to eat you "+namelist.title())
print("delicious!\n")

for value in range(1,5):
    print(value)
print(list(range(1,5)))
print(list(range(2,11,2)))
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares=[value**2 for value in range(1,11)]
print(squares)
print("\n")

players=['charles','martina','micheal','florence','eli']
print(players)
print(players[:4])
print(players[1:])
print(players[-2:])
for player in players[:3]:
    print(player)
my_food=['chiken','steak','pizza']
friend_food=my_food[:]
print(my_food)
print(friend_food)
my_food.append('potato')
friend_food.append('ice')
print(my_food)
print(friend_food)
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)
dimensions=(100,50)
print(dimensions)
print("\n")

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
print("You admission cost is $"+str(price)+".")