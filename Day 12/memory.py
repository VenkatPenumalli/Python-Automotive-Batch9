def large_num(n):
    for i in range(n):
        yield i
gen = large_num(100000)
print(next(gen))
print(next(gen))
print(next(gen))

#basic list comprehension
list = [x*x for x in range(5)]
print(list)
#Comprehension using generator 
gen = (x*x for x in range(5))
print(gen)
