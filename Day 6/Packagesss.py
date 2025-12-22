import PacforSI

def SimpleInterest(P,T,R):
    Total = PacforSI.mul(P,T,R)
    SI = PacforSI.div(Total,100)
    return SI

P = float(input("Enter the Principle amount :: "))
R = float(input("Enter the Rate of Interest :: "))
T = float(input("Enter the time :: "))
result = SimpleInterest(P,T,R)
print("Simple Interest ::",result)