FruitSet = {"Pomogranite","Strawberry","Pineapple","Gauva",False,2,2}
print(FruitSet)
empty_set = set()
empty_dict = {}
print(type(empty_set))
FruitSet.add(10)
FruitSet.discard(10)
FruitSet.update(FruitSet)
for fruit in FruitSet:
    print(fruit)