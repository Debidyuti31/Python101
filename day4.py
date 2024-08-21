#Create a python program to find out whether a person is eligible to vote or not by inputting name and age.
x = input("Enter your name: ")
y = int(input("Enter your age: "))
if (y>=18):           #Check if the person is above or equal to 18yrs
    if (y<100):
        print(x+" you are eligible to cast a vote. Go ahead.")
    else:
        print("you can't cast a vote")
else:                 #person not eligible
    print(x+" you are under-aged. You cannot cast a vote.")
