from datetime import datetime

class VisitorRegister:
    def __init__(self):
        self.visitors = []
    def add_visitor(self):
        name = input("Enter the visitor's name: ").strip()
        company = input("Enter the company: ").strip()
        person_meet = input("Enter the person to meet: ").strip()
        date_input = input("Enter visit date (YYYY-MM-DD): ").strip()
        visit_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        visitor = {
            "name": name,
            "company": company,
            "person_meet": person_meet,
            "date": visit_date
        }

        self.visitors.append(visitor)
        print("✅ Entry Successful\n")
    def search_by_date(self):
        date_input = input("Enter the date to search (YYYY-MM-DD): ").strip()
        search_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        found = False
        print(f"\n📅 Visitors on {search_date}:\n")
        for visitor in self.visitors:
            if visitor["date"] == search_date:
                found = True
                print(f"Name    : {visitor['name']}")
                print(f"Company : {visitor['company']}")
                print(f"Meet    : {visitor['person_meet']}")
                print("-" * 30)
        if not found:
            print("No visitors found for this date.")
    def show_menu(self):
        print("\nVisitor Register System")
        print("1. Add Visitor Entry")
        print("2. Search Visitors by Date")
        print("3. Exit")
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_visitor()
            elif choice == "2":
                self.search_by_date()
            elif choice == "3":
                print("\n Exiting Visitor Register. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
register = VisitorRegister()
register.run()