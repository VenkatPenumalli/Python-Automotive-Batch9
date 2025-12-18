Count_Even = 0
Count_Odd = 0
Even_numli = []
Odd_numli = []
for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    if num % 2 == 0:
        Count_Even += 1
        Even_numli.append(num)
    else:
        Count_Odd += 1
        Odd_numli.append(num)
print(f"Count of Even : {Count_Even}")
print(f"Even Numbers Entered : {Even_numli}")
print(f"Odd Numbers Entered : {Odd_numli}")
print(f"Count of Odd : {Count_Odd}")