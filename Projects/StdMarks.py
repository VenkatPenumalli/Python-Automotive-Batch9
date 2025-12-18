"""
G3.  Student Marks Analysis
You are given the marks of 5 subjects.
Write a program to:
1. Calculate total marks
2. Calculate percentage
3. Determine grade (A/B/C/Fail)
4. Store results in a file
"""

#Student Name
Name = str(input("Student Name :: "))
#SubjectWise Marks
Maths = float(input("Maths :: "))
Python = float(input("Python :: "))
Automata = float(input("Automata :: "))
ML = float(input("ML :: "))
DataAnalytics = float(input("Data Analytics :: "))

#Total
Total = sum([Maths,Python,Automata,ML,DataAnalytics])

#Percentage
Percentage = (Total/500)*100

#Grade
if Percentage >= 90:
    Grade = "A"
elif Percentage >= 70:
    Grade = "B"
elif Percentage >= 60:
    Grade = "C"
elif Percentage >=40:
    Grade = "D"
else:
    Grade = "Fail"

with open("Student_Results.txt","w") as file:
    file.write("Student Marks Report\n")
    file.write(f"Student: {Name}\n")
    file.write(f"Maths : {Maths}\n")
    file.write(f"Python : {Python}\n")
    file.write(f"Automata : {Automata}\n")
    file.write(f"ML : {ML}\n")
    file.write(f"Data Analytics : {DataAnalytics}\n")
    file.write(f"Total Marks : {Total}\n")
    file.write(f"Percentage : {Percentage}\n")
    file.write(f"Grade : {Grade}\n")

print("Student Name :: ", Name)
print("Total Marks Scored :: ", Total)
print("Percentage Scored :: ", Percentage)
print("Grade Scored :: " , Grade)
print("Results Stored Succenfully in StdResults Text file")