class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year

my_car = Car("Honda", "civic", 2020)
print(my_car._year)

my_car.year = 2018
print(my_car._year)

class Student:
    def __int__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa

student_ali = Student("1234", "Ali", 15, 3.95)


class Backpack:

    def __int__(self):
        self._items = []

my_backpack = Backpack()

print(my_backpack._items)


class Movie:

    id_counter = 1

    def __int__(self, title, year, language, rating):
        self.id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1

my_movie = Movie("Star wars", 2020, english, 9.0)

print(my_movie._id)

#https://docs.python.org/3/tutorial/classes.html#private-variables

class PC:

    def __int__(self):
        self.__disk = ["folder"]

my_PC = PC()
print(my_PC._PC__disk)