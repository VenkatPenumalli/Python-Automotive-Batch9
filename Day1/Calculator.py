def cal(a, b, cal):
    match Operator:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a-b
        case "2":
            return "Invalid entry"
a = float(input("Enter 1st number :: "))
b = float(input("Enter 2st number :: "))
Operator = input("ENter the Operator :: ")
result = cal(a,b,Operator)
print("Result :: ", result )