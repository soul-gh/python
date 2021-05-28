guaiguai = {'first_name':'fei','last_name':'wang','age':'26','city':'tokyo'}
print(guaiguai)
favorate_nums = {
    'dingding':'1',
    'dixi':'2',
    'lala':'3',
    'po':'4'
    }
print(favorate_nums)
dictionary = {
    'for':'loop',
    'sort':'order',
    'title':'capital letter',
    'print':'display'
    }
print("'For' means " + dictionary['for']+'.')
print("'Sort' means " + dictionary['sort']+'.')
print("'Title' means " + dictionary['title']+'.')
print("'Print' means " + dictionary['print']+'.')

rivers = {
    'changjiang':'china',
    'nile':'egypt',
    'mississippi':'america',
}
for river, country in rivers.items():
    print("The "+river.title()+"runs through "+country.title())
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
favorate_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
research = ['sarah','jen','phil','lala']
for key in research:
    if key in favorate_languages.keys():
        print(key.title() + ", thanks for join us.")
    else:
        print(key.title()+", please join us.\n")

guaiguai = {'first_name':'fei','last_name':'wang','age':'26','city':'tokyo'}
babi = {'first_name':'ba','last_name':'bi','age':'28','city':'xian'}
mami = {'first_name':'ma','last_name':'mi','age':'27','city':'beijing'}
people = [guaiguai,babi,mami]
for  tomo in people:
    print(tomo)
pet_1 = {'owner':'dingding','type':'dog'}
pet_2 = {'owner':'dixi','type':'cat'}
pet_3 = {'owner':'lala','type':'monkey'}
pets =[pet_1,pet_2,pet_3]
for pet in pets:    
    print(pets)
favorate_place ={
    'dingding':['japan','china','america'],
    'dixi':['tokyo','england'],
    'lala':['xian'],
}
for name,place in favorate_place.items():
    print(name.title()+" favorate place:")
    for basho in place:
        print("\t"+basho)
favorate_nums = {
    'dingding':['1','5','8'],
    'dixi':['2','7'],
    'lala':['3','9'],
    'po':['4']
    }
for name, nums in favorate_nums.items():
    print(name.title()+"'s favorate nums:")
    for num in nums:
        print("\t"+num)
cities = {
    'tokyo':{
        'country':'japan',
        'population':13960000,
        'fact':'small',
    },
    'beijing':{
        'country':'china',
        'population':21540000,
        'fact':'history',
    },
    'newyork':{
        'country':'america',
        'population':8420000,
        'fact':'shine',
    },
}
for city,info in cities.items():
    print(city.title()+":")
    print("\tcountry:"+info['country'].title())
    print("\tpopulation:"+str(info['population']))
    print("\tfact:"+info['fact'])