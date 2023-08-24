#Considering the code below, write code that prints out True! if the largest element of the first range minus the second element of the 3rd range is equal to the first element of the first range, prints out False! if the length of the first range minus the length of the 2nd range is equal to the first element of the 3rd range, prints out Maybe! if the sum of all the elements of the 3rd range divided by 2 returns a remainder of 0, and prints out None! otherwise.

x = [list(range(5)), list(range(5, 9)), list(range(1, 10, 3))]

if max(x[0]) - x[2][1] == x[0][0]:
    print("True!")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("False!")
elif sum(x[2]) % 2 == 0:
    print("Maybe!")
else:
    print("None!")