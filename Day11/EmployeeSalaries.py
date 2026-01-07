class EmployeeSalary:
    def __init__(self):
        self.SalaryList = []
    def get_salary_details(self):
        No_of_Employees = int(input("Enter the number of Employees :: "))
        for i in range(No_of_Employees):
            salary = int(input("Enter the salaries :: "))
            self.SalaryList.append(salary)
    def calculate_salary(self):
        Total_Salaries = sum(self.SalaryList)
        Average_Salary = Total_Salaries / len(self.SalaryList)
        Heighest_Salary = max(self.SalaryList)
        Least_Salary = min(self.SalaryList)
        print(f"The Total Salary of Employees :: {Total_Salaries}")
        print(f"The Average Salary of all the Employees :: {Average_Salary}")
        print(f"Heighest Salary of all the employees :: {Heighest_Salary}")
        print(f"Least Salary of all the Employees :: {Least_Salary}")
emp = EmployeeSalary()
emp.get_salary_details()
emp.calculate_salary()