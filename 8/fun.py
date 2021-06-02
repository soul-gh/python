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