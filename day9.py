#Write a program in python to calculate the simple interest of an user input amount with its rate of interest per annum and time period in years.
a = float(input("Enter P: "))  #Enter Principal Amount
b = float(input("Enter R: "))  #Enter Rate of Interest
d = str(input("Do you want to input time in years? (y/n): "))   #T indicates time
if d == "y":
    c = int(input("Enter T(in years): "))
else:
    f = int(input("Enter T(in months): "))
    c = int(f/12) #convert months to yrs
    print("T in years: ", c)
calculate_simple_interest = float((a*b*c)/100) #formula to calculate Simple Interest
print(calculate_simple_interest)
print("Total amount: ", calculate_simple_interest + a) #Total amount = SI + P
