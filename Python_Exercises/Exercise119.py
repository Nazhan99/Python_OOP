#Considering the code below, write code that prints out True! if one of the following two conditions are satisfied and prints out False! otherwise.

#the third string of the first list in x ends with the letter h
#the second string of the second list in x also ends with the letter h

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("True!")
else:
    print("False!")