#Write a python program to calculate compound interest on an amount with rate of interest over a time period.
#A = P (1 + R/N) ^ nt
p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest (in %): "))
n = float(input("Enter no.of times interest is compounded(per year): "))
t = float(input("Enter number of time periods elapsed(in years): "))

r = (r/100)
amount = p * (1 + r/n) ** (n * t)
compoundInterest = amount - p
print(f"The compound interest is: {compoundInterest:.2f}")

"""
     principal: Initial amount of money
     rate: Annual interest rate 
     time: Time the money is invested for (in years)
     n: Number of times interest is compounded per year
    return: Compound interest
"""