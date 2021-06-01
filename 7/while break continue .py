#message = input("Tell me something, and I will repeat it back to you:")
#print(message)
#name = raw_input("please enter your name: ")
#print("Hello, " + name +"!")
#prompt = "If you tell us who you are, we can personlize the messages you see."
#prompt += "\nWhat is your first name?"
#name = raw_input(prompt)
#print("Hello, "+ name + "!")
#age = input("How old are you?")
#print(int(age) >= 18)
#height = input("How tall are you, in inches?")
#height =int (height)
#if height >= 36:
#    print("You are tall enough to ride.")
#else:
#    print("Sorry")
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#if number % 2 == 0:
#    print("The number " + str(number) + " is even.") 
#else:
#    print("The number " + str(number) + " is odd.") 

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active :
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
while True :
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+".")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)