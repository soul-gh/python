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
    print("You really like paneapple.\n")

#users=['admin','tom','jerry','dingding','lala']
users=[]
if users:
    for user in users:   
        if user == 'admin':
            print("Hello Admin, would you like to see a status report?")
        else :
            print("Hello "+user.title()+", thank you for logging in again.")
else :
    print("We need to find some users.")

current_users=['admin','tom','jerry','dingding','lala']
new_users=['admin','Tom','dixi','po','makabaka']
for new_user in new_users:
    if new_user in current_users:
        print("Please enter another username.")
    elif new_user.lower() in current_users:
        print("Please enter another username.")
    else :
        print(new_user+" haven't been used.")
nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num == 1:
        print(str(num)+"st")
    elif num == 2:
        print(str(num)+"nd")
    elif num == 3:
        print(str(num)+"rd")
    else:
        print(str(num)+"th")