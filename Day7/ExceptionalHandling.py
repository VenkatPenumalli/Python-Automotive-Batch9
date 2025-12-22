try:
    num = int(input("Enter the number :: "))
    result = 10/num
    print("Result :: ",result)
except ZeroDivisionError:
    print("The divisor cannot be 0")
except ValueError:
    print("The divisor is non numeric")
finally:
    print("Everything Done")