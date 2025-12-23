class Person:
    def __init__(self,id):
        self.id = id
class Student(Person):
    def EvenPart(self):
        return self.id % 2 == 0
ListID = list(map(int,input("Enter students :: ").split()))
students = []
for i in ListID:
    students.append(Student(i))
EvenID = []
OddID = []
for s in students:
    if s.EvenPart():
        EvenID.append(s.id)
    else:
        OddID.append(s.id)
print("First Round Participants : ",EvenID)
print("Second Round Participants : ",OddID)
