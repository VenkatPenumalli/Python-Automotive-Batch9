class Employee:
    def __init__(self,Employee_ID,Name,Basic_Salary):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.Basic_Salary = Basic_Salary

    def Calculate_HRA(self):
        return self.Basic_Salary*0.20
    def Calculate_DA(self):
        return self.Basic_Salary*0.10
    def Calculate_Net_Salary(self):
        HRA = self.Calculate_HRA()
        DA = self.Calculate_DA()
        Net_Salary = self.Basic_Salary + HRA + DA
        return Net_Salary

Employee_ID = int(input("Enter Employee ID: "))
Name = input("Enter Employee Name: ")
Basic_Salary = float(input("Enter Basic Salary: "))

Payroll = Employee(Employee_ID, Name, Basic_Salary)

print("HRA:",Payroll.Calculate_HRA())
print("DA:",Payroll.Calculate_DA())
print("Net Salary:",Payroll.Calculate_Net_Salary())
