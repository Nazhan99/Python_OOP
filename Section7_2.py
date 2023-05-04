class Dog:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        print("Calling the getter...")
        return self._age

    def set_age(self, new_age):
        print("Calling the setters...")
        if isinstance(new_age, int) and 0 <new_age<30:
            self._age = new_age

        else:
            print("Please enter valid age.")

    age = property(get_age, set_age)

my_dog = Dog(8)

print(f"My dog is {my_dog.get_age()} years old")
print("One year later...")

my_dog.age +=1
print(f"My dog is {my_dog.get_age()} years old")

class Circle:

    VALID_COLORS = ["Blue", "Red", "Green"]

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius

        else:
            print("Please enter a valid radius.")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter valid color")

my_radius = Circle(8, "Blue")
print(my_radius.get_radius())
my_radius.radius = 16
print(my_radius.get_radius())

my_radius.color = "Red"
print(my_radius.color)

