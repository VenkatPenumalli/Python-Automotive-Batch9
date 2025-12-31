from functools import reduce 
print("Using Lambda Functions")
x = lambda a:a+10
print(x(5))
y = lambda a,b: a*b
print(y(2,3))
z = lambda a,b,c : a+b+c
print(z(1,2,3))
a = [1,2,3,4,5]
b = map(lambda x:x**2,a)
print(list(b))
c = reduce(lambda f,g:f+g, a)

#import reduce
#define lambds : must accept 2 arguments
#call reduce
