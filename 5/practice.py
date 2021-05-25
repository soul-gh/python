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