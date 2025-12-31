def abc():
    yield 1  #yield makes a definition to convert into generator
    yield 2   
    yield 3

for value in abc(2):
    print(value)

def count(n):
    c = 1 #reference value
    while c<=n:
        yield c
        c+=1
for num in count(4):
    print(num)
