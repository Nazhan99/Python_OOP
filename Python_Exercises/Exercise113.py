#Considering the code below, write code that prints out True! if x is a string and the first character in the string is T.

x = "The days of Python 2 are almost over. Python 3 is the king now."

if type(x) is str and x.startswith("T"):
    print("True!")