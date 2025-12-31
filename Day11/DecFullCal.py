def calculator(func):
    def nums(a,b,choice):
        if choice == "+":
            result = a + b 
        elif choice == "-":
            result = a - b
        elif choice == "*":
            result = a * b 
        elif choice == "/":
            result = a / b
        else:
            return "Enter a Valid Choice"
        return func(result)
    return nums
@calculator
def answer(result):
    return f"Solution is {result}"
a = float(input("Enter a: "))
b = float(input("Enter b: "))
Choice = input("Enter an Operator: ")
print(answer(a,b,Choice))