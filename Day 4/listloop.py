Food = ["Pizza", "Hamburger","HotDog","Spaghetti"]
print(Food)
print(Food[1])
Food[0] = "Fries"
print(Food)
Food.append("Appricort Delight")
print(Food)
Food.remove("Spaghetti")
print(Food)
Food.pop()
Food.pop(1)
Food.insert(0,"Cake")
Food.sort()
Food.clear()
for i in Food:
    print(i)
"""
Numlist = [1,2,3,4,5]
for i in Numlist:
    print(i*Numlist)
"""