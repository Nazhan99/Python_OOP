class Circle:

    def __int__(self, radius, colors):
        self.radius = radius
        self.colors = colors


pass


my_circle = Circle(6, "Yellow")

print(my_circle.radius)
print(my_circle.colors)

my_circle.radius = 15
my_circle.colors = "Red"

print(my_circle.radius)
print(my_circle.colors)


class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color
pass

my_backpack = Backpack("Blue")
print(my_backpack.color)
