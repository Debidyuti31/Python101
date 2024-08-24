#Write a python program for Calculating the Volume of Cube or Cuboid using 'if' conditional statement.
a = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
c = float(input("Enter the depth: "))
calculated_volume = float(a*b*c)
if (a == b):
    if (a == c):
        print("Volume of CUBE : ")
        print(calculated_volume)
else:
    print("Volume of CUBOID : ")
    print(calculated_volume)