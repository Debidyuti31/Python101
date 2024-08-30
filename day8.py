#Write a python program to input a number and print the entire multiplicative table of that number from 1 to 10 using range function only.
a = int(input("Enter Number: "))
x = range(1,11)
print("Multiplicative table of given number:")
for n in x:
    print(a,"x",n,"=",a*n)
    