#Considering the code below, write code that prints out True! if the second to last character of the value at key 3 is the first character of the value at key 5, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[3][-2] == x[5][0]:
    print("True!")
else:
    print("False!")