# program to return days of the month by inputting respective numbers using dictionary
#defining dictionary key & value pairs
this_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 
    8: "August", 9: "September",10: "October",11: "November",12: "December"
}
a = int(input("Enter month number : "))   #user input
print(this_dict[a])
