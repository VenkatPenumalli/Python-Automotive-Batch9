SalaryList = []
No_of_Employees = int(input("Enter the number of Employees :: "))
for i in range(No_of_Employees):
    salary = int(input("Enter the salaries :: "))
    SalaryList.append(salary)
Total_Salaries = sum(SalaryList)
"""for salary in SalaryList:
    Total_Salaries += salary"""
Average_Salary = Total_Salaries/len(SalaryList)
Heighest_Salary = max(SalaryList)

Least_Salary = min(SalaryList)
print(f"The Total Salary of Employees :: {Total_Salaries}")
print(f"The Average Salary of all the Employees :: {Average_Salary}")
print(f"Heighest Salary of all the employees :: {Heighest_Salary}")
print(f"Least Salary of all the Employees :: {Least_Salary}")


