ManagerDict = {
    "Manager1": [
        {"Name": "Venkat", "Score": 85},
        {"Name": "Ram", "Score": 90},
        {"Name": "Rahim", "Score": 68},
        {"Name": "Robert", "Score": 75}
    ],
    "Manager2": [
        {"Name": "Rahul", "Score": 60},
        {"Name": "Suman", "Score": 65},
        {"Name": "Saman", "Score": 85},
        {"Name": "Varun", "Score": 80}
    ],
    "Manager3": [
        {"Name": "Emp1", "Score": 85},
        {"Name": "Emp2", "Score": 60},
        {"Name": "Emp3", "Score": 78},
        {"Name": "Emp4", "Score": 55}
    ]
}
Pass_Score = 75
Passed_Performers = {
    manager: list(filter(lambda emp: emp["Score"] >= Pass_Score, employees))
    for manager, employees in ManagerDict.items()
}
print("Employees Passed with the given criteria:\n")

for manager, employees in Passed_Performers.items():
    print(manager)
    for emp in employees:
        print(f"  {emp['Name']} - Score: {emp['Score']}")
    print()
