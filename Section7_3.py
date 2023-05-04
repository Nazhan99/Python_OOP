class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 0.0 <= new_rating <= 10.0:
            self._rating = new_rating

        else:
            print("Please enter a valid rating.")

my_movie = Movie("Star wars", 9)
print(my_movie.rating)

my_movie.rating = 8.1
print(my_movie.rating)


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter valid list")

my_backpack = Backpack()
print(my_backpack.items)

my_backpack.items = ["Pencils", "laptop", "books"]
print(my_backpack.items)

