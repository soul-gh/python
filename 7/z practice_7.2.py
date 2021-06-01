while True:
    message = input("Please enter your topping:")
    if message == 'quit':
        print("Thanks for your order.")
        break
    else :
        print("OK, you ordered " + message.title()+".")

message = ""
while message != 'quit':
    message = input("Please enter your topping:")
    if message != 'quit':
        print("OK, you ordered " + message.title()+".")


while True:
    message = input("Please enter your age:")
    if message == 'quit':
        break
    elif int(message) < 3:
        print("free")
    elif int(message) >=3 and int(message) <= 12:
        print("10$")
    else:
        print("15$")

active = True
while active:
    message = input("Please enter your age:")
    if message == 'quit':
        active = False
    elif int(message) < 3:
        print("free")
    elif int(message) >=3 and int(message) <= 12:
        print("10$")
    else:
        print("15$")

num = 0
while num <=10:
    if num % 2 == 0:
        print(num)
    num += 1

