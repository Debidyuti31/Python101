#Create a program to calculate Body-Mass Index of a person taking in person's weight and height and calculate BMI.
a = float(input("Enter Height(in metres):"))
print("Height = ", a)
b = float(input("Enter Weight(in kg):"))
print("Weight = ", b)
#BMI = weight/height*2
BMI = float(b//(a*a))
print(BMI)

if (BMI < 18.5):
    print("Underweight")
elif (BMI > 18.5 and BMI < 24.9):
    print("Normal weight")
elif (BMI > 25 and BMI < 29.9):
    print("Overweight")   
elif (BMI > 30):
    print("Obese") 