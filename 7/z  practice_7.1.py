car = input("Which car are you seeking?")
print("Let me see if I can find you a " + car + ".")
people = input("How many people?")
people = int(people)
if people >= 8:
    print("Sorry, we have no table for you.")
else:
    print("OK")
num = input("Please enter a number: ")
num = int(num)
if num %10 == 0:
    print("It is multiples of ten.")
else:
    print("It is not multiples of ten.")
