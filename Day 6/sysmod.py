import sys
NumberList = list(map(int, sys.argv[1:]))
total = sum(NumberList)
average = total/len(NumberList)
print("Numbers Entered :: ",NumberList)
print("Sum of numbers ::",total)
print("Average ::",average)
