class Circle:

    def __init__(self,radius):
        self.radius = radius

    def find_diameter(self):
        print(f"Diameter: {self.radius * 2}")
        return self.radius * 2

class Backpack:

    def __init__(self):
        self.items = []

    @property
    def items(self):
        return self.items

    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)

        else:
            print("Please add a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items

    