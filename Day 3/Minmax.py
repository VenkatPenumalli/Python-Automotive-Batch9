print("Get max, min swap value of variables")
print("\n 1.Max 2.Min \nn3.Swap")
a,b = map(int,input("Enter two numbers ").split(","))
choice = int(input("Enter your choice"))
if(choice == 1):
    print(max(a,b))
elif(choice==2):
    print(min(a,b))
elif(choice==3):
    a,b = b,a
    print("After swaping %d %d " %(a,b))
else:
    print("Invalid Choice")