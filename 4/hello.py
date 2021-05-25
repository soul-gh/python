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

