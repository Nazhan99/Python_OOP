class Circle:
    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(4)
your_circle = my_circle

print("Before: ")
print(my_circle.radius)
print(your_circle.radius)

your_circle.radius = 18

print("Before: ")
print(my_circle.radius)
print(your_circle.radius)


class Backpack:

    def __int__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print("This item is not in the backpack")


my_backpack = Backpack()
your_backpack = my_backpack
her_bakpack = your_backpack

print(my_backpack is your_backpack is her_bakpack)

my_backpack.add_item("WaterBottle")
my_backpack.add_item("Pencil")

print(my_backpack.items)
print(your_backpack.items)
print(her_bakpack.items)