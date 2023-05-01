class Backpack:

    def __init__(self, color, size):
        self.items = ["water_bottle", "pencils"]
        self.color = color
        self.size = size
        print(self.items)
pass

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.color = "Blue"
pass

class Rectangle:

    def __init__(self,length, width):
        self.length = length
        self.width = width
pass

class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating
pass


my_backpack = Backpack("Blue",5)


my_circle = Circle(24)
print(my_circle)



