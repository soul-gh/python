#字符串列表分割
def split1(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')

a = ['1','2 3 4','5 6 7']
print(a)
split1(a)
print(a)

#列表内所有元素 字符串转整数
a = [list(map(int,x)) for x in a]
print(a)
a = [list(map(str,x)) for x in a]
print(a)