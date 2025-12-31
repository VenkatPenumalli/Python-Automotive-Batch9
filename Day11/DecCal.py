def Calculator(func):
    def nums(a, b):
        result = a + b
        return func(result)
    return nums
@Calculator
def decresult(addi):
    print("Sum of two numbers:", addi)
decresult(5, 4)
