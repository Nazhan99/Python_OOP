#Considering the code below, write code that prints out True! if the length of the first range is greater than or equal to 5, prints out False! if the length of the second range is 4, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if len(x[0]) >= 5:
    print("True!")
elif len(x[1]) == 4:
    print("False!")
else:
    print("None!")