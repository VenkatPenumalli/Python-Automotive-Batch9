"""
write a python program that will have usecase of school 
having 20 student and we have to find out that student 
whose name is the same with another student but ser-name 
is different maintain only one dublicate
""" 
li = [("Venkat","Penumalli"),("Ram","Laxman"),("Ram","Mishra"),
      ("Krishna","Vasudev"),("Hari","Nandan"),("Sharukh","Shaik")
      ("Farukh","Mohamudd"),("Hardik","Gorla"),("Venu","Maturi")
      ("Mahesh","Babu"),("Chris","Evans"),("Cristian","Bale")]

for name, surname in li:
    First = {name}
    Second = [surname]
    if name not in First:
        First[name] = surname
    else:
        Second.append(name)
