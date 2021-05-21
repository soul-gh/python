brands=['nike','adidas','puma']
print(brands[0])
print(brands[1].title())
print(brands[-1])
print(brands[-2])
message="I like "+brands[-3].title()+"."
print(message)
print("\n")

print(brands)
brands[0]='lining'
print(brands)
brands.append('nike')
print(brands)
brands.insert(0,'supreme')
print(brands)
del brands[0]
print(brands)
del brands[2]
print(brands)
favorate_brand=brands.pop()
print(brands)
print(favorate_brand)
print("My favorate brand is "+favorate_brand.title()+".")
brands.append('nike')
print(brands)
print("I like "+brands.pop(1)+".")
print(brands)
brands.append('adidas')
print(brands)
brands.remove('nike')
print(brands)
too_expensive='lining'
brands.remove(too_expensive)
print(brands)
print("A "+too_expensive.title()+" is too expensive to me.\n")

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)
print(len(cars))
print("\n")

