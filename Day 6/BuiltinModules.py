from math import sqrt,factorial
print("Square root is ",sqrt(36))

import random
print("A random number from 1 to 50 :: ",random.randint(1,50))


import requests
r = requests.get("https://www.google.com")
r.status_code