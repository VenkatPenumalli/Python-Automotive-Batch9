Students = [100,90,80,70,60,50,40,30,20,10,0]
pass_students = [i if i>60 else "Failed" for i in Students]
print(pass_students)