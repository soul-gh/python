from typing import Collection


def city_country(city,country):
    print(city.title() + "," + country.title())
city_country('santiago', 'chile')
city_country(city='beijing',country='china')
city_country(country='japan',city='tokyo')

def make_album(name,collection,number=''):
    album = {'name':name, 'collection':collection}
    if number:
        album['number'] = str(number)
    return album
MJ = make_album('MJ','thrill','10')
print(MJ)
Jay = make_album('Jay','fantacy')
print(Jay)

while True:
    print("You can quit at any time by enter 'q'.")
    name = input("Please enter singer's name:")
    if name == 'q':
        break
    collection = input("Please enter his or her collection:")
    if collection == 'q':
        break
    info = make_album(name,collection)
    print(info)


