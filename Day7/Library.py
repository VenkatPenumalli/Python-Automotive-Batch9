class Library:

    def __init__(self,Stack,geners):
        self.Stack = Stack
        self.geners = geners

    def Description(self):
        return f"Stack {self.Stack} has {self.geners} gener books"

book1 = Library("A","Computer Science")
book2 = Library("B","Science Fiction")    

print(book1.Description())
print(book2.Description())