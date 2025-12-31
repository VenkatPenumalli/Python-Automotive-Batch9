"""
E-Commerce Discount Engine
Use Case
An online store offers Seasonal, Festival, and Coupon discounts.
Task
•	Base class Discount
•	Override apply_discount(amount)
Polymorphism
Apply discounts dynamically at checkout.
"""

class Discount:
    def __init__(self,Amount):
        self.Amount = Amount
    def apply_discount(self,Amount):
        return Amount

class Festival_Discount(Discount):
    def apply_discount(self, Amount):
        return Amount - (Amount * 0.20)

class SeasonalDiscount(Discount):
    def apply_discount(self, Amount):
        return Amount - (Amount * 0.10)

class Coupon_Discount(Discount):
    def apply_discount(self, Amount):
        return Amount - 100
def checkout(Amount, discount_obj):
    Final_Price = discount_obj.apply_discount(Amount)
    return Final_Price
Amount = float(input("ENter the Amount :: "))
print("1.Festival Discount")
print("2.Seasonal Discount")
print("3.Coupon Discount")
choice = int(input("Choose Discount type: "))
if choice == 1:
    discount = Festival_Discount()
elif choice == 2:
    discount = SeasonalDiscount()
elif choice == 3:
    discount = Coupon_Discount()
else:
    discount = Discount()

Price = checkout(Amount,discount)
print("Final Amount to Pay :: ",Price)