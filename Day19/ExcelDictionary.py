from openpyxl import Workbook
D1 = {"Venkat":"E1"}
D2 = {"E1":"P1"}
sheet = Workbook()
sheetactive = sheet.active
sheetactive.title = "Employee Details"
sheetactive.append(["Employee Name","EID","Computer Name"])
for name, eid in D1.items():
    if eid in D2:
        Computername = D2[eid]
        sheetactive.append([name,eid,Computername])
file_path = r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day19\EmployeeDetails.xlsx"
sheet.save(file_path)
print("!...Sheet created...!",file_path)