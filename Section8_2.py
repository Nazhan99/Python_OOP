my_list = [4, 5, 6, 7, 8]

my_list.append(14)

print(my_list)

my_list.extend([1, 2, 3])
print(my_list)

my_list.sort()
print(my_list)

number = my_list.pop()
print(number)



class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        return self.radius * 2

my_circle = Circle(2)
diameter = my_circle.find_diameter()
print(diameter)