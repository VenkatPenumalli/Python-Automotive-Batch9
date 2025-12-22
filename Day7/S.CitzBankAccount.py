class BankAccount:
    def _init_(self,Principal,Time,Age):
        self.P = Principal
        self.T = Time
        self.age = Age
    def CompundInterest(self):
        if self.age >= 60:
            rate = 8
            CompInterest = self.P +(self.P*rate*self.T)/100
            return f"Compound Interest for Senior Citizen :: {CompInterest}"    
        else:
            return "Must be a Senior Citizen"
principalamount = float(input("Enter Principal Amount :: "))
timeinyears = float(input("Enter Time in years :: "))
Age = float(input("Enter the Age"))

Account = BankAccount(principalamount,timeinyears,Age)
print(Account.CompundInterest())