def greet_user(username):
    print("Hello," + username.title()+"!")
greet_user('dixi')

def describe_pet(animal_type,pet_name):
    #顺序实参
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('cat','lala')
describe_pet('dog','dixi')
print("\n")

def describe_pet(animal_type,pet_name):
    #关键字实参
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type = 'cat',pet_name = 'lala')
describe_pet(pet_name = 'lala',animal_type = 'cat')
print("\n")

def describe_pet(pet_name,animal_type = 'dog'):
    #默认值
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('dixi')
describe_pet(animal_type = 'cat',pet_name = 'herry')
print("\n")

#返回值
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#返回字典
def build_person(first_name, last_name, age = ''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix',age = 27)
print(musician)

#函数与while
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
while True:
    print("Please tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First_name:")
    if f_name == 'q':
        break
    l_name = input("Last_name:")
    if l_name == 'q':
        break
    full_name = get_formatted_name(f_name,l_name)
    print("Hello, "+full_name)

