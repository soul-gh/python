unconfirmed_users = ['alice','bob','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Varifying user: "+current_user)
    confirmed_users.append(current_user)    
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) 
pets = ['cat','dog','cat','goldfish','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Result ---")
for name ,response in responses.items():
    print(name + "would like to climb " + response + ".")