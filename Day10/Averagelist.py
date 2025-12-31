try:
    n = input()
    if not n.isdigit():
        print("Error: You must enter a numeric value.")
        exit()
    n = int(n)
    if n < 0:
        print("Error: The length of the list must be a non-negative integer.")
        exit()
    numbers = []
    for _ in range(n):
        value = input()
        if not value.lstrip('-').isdigit():
            print("Error: You must enter a numeric value.")
            exit()
        numbers.append(int(value))
    if n == 0:
        average = 0.00
    else:
        average = sum(numbers) / n
    print(f"{average:.2f}")
except Exception:
    print("Error: You must enter a numeric value.")
