sandwich_orders = ['fruits sandwich','pastrami sandwich','chicken sandwich','pastrami sandwich','egg sandwich','pastrami sandwich']
print("Our pastrami sandwich have been sold out.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)
finished_sandwihes = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order.title() + ".")
    finished_sandwihes.append(sandwich_order)
print(finished_sandwihes)

responses = {}
active = True
while active:
    name = input("What's youe name?")
    place = input("Where would you go for a trip?")
    responses[name] = place
    answer = input("Would you like to let another person respond?(yes/no)")
    if answer == 'no':
        active = False
for name, place in responses.items():
    print(name.title() + " want go to " + place.title() + ".")
    
    
