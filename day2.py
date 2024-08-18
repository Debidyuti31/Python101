#Create a python program with a list of 8 different colors keeping the 5th color as white and print the list. Using loop statements breaks the printing of the list when white appears.
colours = ["red", "green", "blue", "yellow", "white", "black", "magenta", "pink"]
for x in colours:
    print (x)
    if x == "white":
        break