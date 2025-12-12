with open("Hey.txt", "w") as file:
    file.write("Hello! This is a sample text.\n")
    file.write("This text is written using Python.\n")

print("Data written to example.txt")

# Reading from the same file
with open("Hey.txt", "r") as file:
    content = file.read()

print("\nFile Contents:")
print(content)