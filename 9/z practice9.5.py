from collections import OrderedDict
favorate_fruits = OrderedDict()
favorate_fruits['dixi'] = 'apple'
favorate_fruits['lala'] = 'banana'
favorate_fruits['dingding'] = 'pear'
for k,v in favorate_fruits.items():
    print(k.title() + " likes " + v + ".")

from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self,times=10):
        for n in range(times):
            print(randint(1,self.sides))
        print("___")
die1 = Die()
die1.roll_die()
die2 = Die(10)
die2.roll_die()
die3 = Die(20)
die3.roll_die(5)