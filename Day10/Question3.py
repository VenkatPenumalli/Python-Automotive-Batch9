# Base class
class BusinessUtility:
    def calculate_margin(self, revenue, cost):
        # Regular Margin = ((Revenue - Cost) / Revenue) * 100
        if revenue == 0:
            return 0.0
        return ((revenue - cost) / revenue) * 100
# Derived class (Inheritance + Method Overriding)
class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self, revenue, cost):
        # Call base class method
        regular_margin = super().calculate_margin(revenue, cost)
        # Add seasonal adjustment of 10%
        seasonal_margin = regular_margin + 10
        return seasonal_margin
# Profitability checker class
class ProfitabilityChecker:
    def check_profitability(self, regular_margin):
        if regular_margin >= 10:
            print("Business is profitable.")
        else:
            print("Business is not profitable.")
# Main Program
# Read inputs
revenue = float(input("Enter Revenue: "))
cost = float(input("Enter Cost: "))
# Create objects
business = BusinessUtility()
seasonal_business = SeasonalBusinessUtility()
checker = ProfitabilityChecker()
# Calculate margins
regular_margin = business.calculate_margin(revenue, cost)
seasonal_margin = seasonal_business.calculate_margin(revenue, cost)
# Display results
print(f"Regular Margin: {regular_margin:.2f}%")
print(f"Seasonal Margin: {seasonal_margin:.2f}%")
# Check profitability
checker.check_profitability(regular_margin)