"""
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
"""


Word = str(input("Enter"))
vowels = "AaEeIiOoUu"
count = 0
for c in Word:
    if c in vowels:
        count += 1
print("No of vowels in ",Word, "are", count)