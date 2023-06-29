#Given the code below, use the correct method on line 4 in order to find out the common elements of my_set1 and my_set2.

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

common = my_set1.intersection(my_set2)

print(sorted(list(common)))