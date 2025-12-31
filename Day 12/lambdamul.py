from functools import reduce
 
numbers = [1, 2, 3, 4, 5]
 
# The lambda x, y: x * y multiplies the current accumulator (x) and the next item (y)
product_result = reduce(lambda x, y: x * y, numbers)
 
print(product_result)
# Output: 120 (calculated as ((((1*2)*3)*4)*5))