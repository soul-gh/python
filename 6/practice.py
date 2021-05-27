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
        print(key.title()+", please join us.")
