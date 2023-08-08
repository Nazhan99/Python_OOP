#Considering the code below, write code that prints out True! if the last 3 characters of the string are all digits and prints out False! otherwise.

#Hint! Use the appropriate method to check if the requested string slice contains digits only.

x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[-3:].isdigit():
    print("True!")
else:
    print("False!")