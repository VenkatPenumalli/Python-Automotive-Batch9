a = int(input("Enter number A :: "))
b = int(input("Enter number B :: "))
def cal(a,b,options):
    Add = a + b 
    Sub = a - b 
    Div = a/b 
    Mul = a*b
    if options == 1:
        print(f"Addition of {a} and {b} is ",Add)
    elif options == 2:
        print(f"Difference of {a} and {b} is ",Sub)
    elif options == 3:
        print(f"Division of {a} and {b} is ",Div)
    elif options == 4:
        print(f"Product of {a} and {b} is ",Mul)
    else:
        print("Invalid")
options = int(input("Enter the Option :: "))
cal(a,b,options)