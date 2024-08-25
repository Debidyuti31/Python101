# program to return days of the week by inputting respective numbers
def days_of_week(n):  #defining function
    #defining switch case with n as input
    match n:
        case 1:
            return "Sunday" 
        case 2: 
            return "Monday" 
        case 3: 
            return "Tuesday" 
        case 4: 
            return "Wednesday" 
        case 5: 
            return "Thursday" 
        case 6: 
            return "Friday" 
        case 7: 
            return "Saturday"
x = int(input("Enter the number: "))
day = days_of_week(x)  #calling the function and storing it in variable
print(day) #printing function output
