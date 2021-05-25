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

foods=['egg','apple','banana','bread']
food=foods[0]
print("Is food=='egg'?I predict True.")
print(food=='egg')
print("Is food=='apple'?I predict False.")
print(food=='apple')
print('he'!='she')
print(food.title()=='egg')
print('\n')
answer=10
print(answer==10)
print(answer!=10)
print(answer<11)
print(answer>9)
print(answer<=9)
print(answer>=9)
print(answer>=10 and answer<=10)
print(answer>20 or answer<15)
print('\n')
print('egg' in foods)
print('apple'not in foods)
alien_color='yellow'
if alien_color=='yellow':
    print("You got 5 point.")
if alien_color=='green':
    print("You got 5 point.")
alien_color='red'
if alien_color=='green':
    print("You got 5 point.")
elif alien_color=='yellow':
    print("You got 10 point.")
elif alien_color=='red':
    print("You got 15 point.")

age=13
if age<2:
    print("You are baby.")
elif age>=2 and age<4:
    print("You are learning how to stand.")
elif age>=4 and age<13:
    print("You are child.")
elif age>=13 and age<20:
    print("You are teenager.")
elif age>=20 and age<65:
    print("You are adult.")
else:
    print("You are old people.")

favorate_fruits=['apple','banana','kiwi']
if 'apple' in favorate_fruits:
    print("You really like apple.")
if 'banana' in favorate_fruits:
    print("You really like banana.")
if 'kiwi' in favorate_fruits:
    print("You really like kiwi.")
if 'pear' not in favorate_fruits:
    print("You don't like pear.")
if 'paneapple' in favorate_fruits:
    print("You really like paneapple.")