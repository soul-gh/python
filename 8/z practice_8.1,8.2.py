def display_message():
    print("We learned function in this section.")
display_message()
def favorate_book(title):
    print("One fo my favorate book is " + title.title() + ".")
favorate_book('alice in wonderland')
print("\n")

def make_shirt(size,pattern = 'I love python'):
    print("Size:" + str(size))
    print("Pattern:" + pattern)
make_shirt('Xl','Moon')
make_shirt(pattern = 'Moon',size = 'Xl')
make_shirt('XL')
make_shirt(pattern = 'Sun',size = 'XL')
print("\n")

def describe_city(city='Xian',country='China'):
    print(city.title() + " is in " + country.title() + ".")
describe_city()
describe_city('beijing')
describe_city('tokyo','japan')
describe_city(country='america',city='new york')