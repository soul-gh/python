alien_0 = {'color':'green','points':5,'speed':'fast'}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You got " + str(new_points)+" points.")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color']+'.')
print("Original X-positon: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New X-position: " + str(alien_0['x_position']))
print(alien_0)
del alien_0['points']
print(alien_0)
favorate_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("Sarah's favorate language is " + favorate_languages['sarah'].title())
for name, language in favorate_languages.items():
    print(name.title() + "'s favorate language is " + language.title())
for name in favorate_languages.keys():
    print(name)
friends = ['phil','sarah']
for name in favorate_languages:
    if name in friends:
        print("Hi "+name.title()+", I see you favorate language is "+favorate_languages[name].title()+".")
if 'lisa' not in favorate_languages.keys():
    print("Lisa, please take our poll.")
for name in sorted(favorate_languages.keys()):
    print(name.title()+", thank you for taking the poll.")
for language in favorate_languages.values():
    print(language.title())
print("\n")
for language in set(favorate_languages.values()):
    print(language.title())

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
 }
for key, value in user_0.items():
    print("\nKey:" + key)
    print("Value:" + value)
