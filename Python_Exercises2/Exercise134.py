#Considering the code below, write code that prints out True! if the 2nd character of the value at key 1 is also present in the value at key 4, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[1][1] in x[4]:
    print("True!")
else:
    print("False!")