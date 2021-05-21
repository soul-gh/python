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
print("list2:"+str(list2))