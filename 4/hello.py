print("hello git world!\n")
tianxian_baobao=["dingding","dixi","lala","po"]
for namelist in tianxian_baobao:
    print(namelist)
print(namelist)
for namelist in tianxian_baobao:
    print("I like "+namelist.title())
    print("I can't wait to eat you "+namelist.title())
print("delicious!\n")

for value in range(1,5):
    print(value)
print(list(range(1,5)))
print(list(range(2,11,2)))
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares=[value**2 for value in range(1,11)]
print(squares)