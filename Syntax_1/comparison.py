#correct
if 3 > 5:
    print("more") # The body of the if statement is this single line
else :
    print("less") # The body of the else statement is this single line

# Single line if-else statements can be written like this
# However this makes the code unreadable and is discouraged
if 3 > 5: print ("more")
else : print ("less")

# "else if" in python is written as elif
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70:
    print("A")
elif mark > 60: # Note the use of "elif"
    print("B")
elif mark > 50: # Note the use of "elif"
    print("C")
else:
    print("F") 

# Comparison operators are used to compare values