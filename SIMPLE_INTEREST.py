#SIMPLE INTEREST
def SI(p,r,t):
    return p*r*t/100

p=int(input("enter the principal amount="))
r=int(input("enter the rate of interest="))
t=int(input("enter the amount of time(IN YEARS)="))
si=SI(p,r,t)
print("SIMPLE INTEREST=",si)
