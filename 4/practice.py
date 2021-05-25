food=["kfc","mcdonald's","burgerking"]
for fast in food:
    print(fast.title())
    print("I like fried chicken.")
print("I really love chicken")
animal=["monkey","tiger","panda"]
for doubutsu in animal:
    print(doubutsu)
    print("The "+doubutsu+" is cool.")
print("Any of these animals would be found in the zoo.\n")

for num in range(1,21):
    print(num)
''' numbers=list(range(1,1000001))
for va in numbers:
    print(va)
print(min(numbers))
print(max(numbers))
print(sum(numbers))'''
odd=list(range(1,21,2))
print(odd)
for va in odd:
    print(va)

three = list(range(3,31,3))
for vb in three:
    print(vb)
list1=[]
for value in range(1,11):
    list1.append(value**3)
    print(list1[-1])
list2 =[vc**3 for vc in range(1,11)]
print("list2:"+str(list2)+'\n')
''' test '''

brands=['suprene','nike','adidas','puma']
print("The first three brands in the list are:"+str(brands[:3]))
print("The middle two brands in the list are:"+str(brands[1:3]))
print("The last three brands in the list are:"+str(brands[1:]))
friend_food=food[:]
print(friend_food)
food.append('ice_cream')
friend_food.append('wasabi')
print("My favorate food are:")
for food1 in food:
    print(food1)
print("My friend favorate food are:")
for food1 in friend_food:
    print(food1)
print("\n")

supermarket=('egg','milk','snack','apple','banana')
for food1 in supermarket[:]:
    print(food1)
print("\n")
supermarket=('egg','milk','potatochips','panapple','banana')
for food1 in supermarket:
    print(food1)
print('\n')

