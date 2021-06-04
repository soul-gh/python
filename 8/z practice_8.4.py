magicians = ['liuqian','david','guohao']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
show_magicians(magicians)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the great '+ magicians[i]
make_great(magicians)
print(magicians)
print("\n")

current_magicians = []
magicians = ['liuqian','david','guohao']
def make_great1(magicians,current_magicians):
    for magician in magicians:
        magician = 'the great' + magician
        current_magicians.append(magician)
make_great1(magicians,current_magicians)
show_magicians(magicians)
show_magicians(current_magicians)