x = int(input("Enter the number :: "))
if x <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            is_prime = False
            break
    print(is_prime)