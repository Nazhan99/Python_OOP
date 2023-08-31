#Considering the code below, write code that prints out True! if the number of characters of the smallest value in the dictionary is equal to the number of occurrences of letter a in the value at key 3, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if len(min(x.values())) == x[3].count("a"):
    print("True!")
else:
    print("False!")