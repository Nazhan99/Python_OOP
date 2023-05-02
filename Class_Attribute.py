#class ClassName:

#Class Attributes
#__init__()
#Methods
#pass

class Dog:

    species = "Canis lupus"

    def __int__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
pass

print(Dog.species)

class Backpack:

    max_num_items = 10

    def __int__(self):
        self.items = []

my_backpack = Backpack()
your_backpack = Backpack()

print(my_backpack.max_num_items)
print(your_backpack.max_num_items)

Backpack.max_num_items = 15
print(Backpack.max_num_items)

class Movie:

    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1

my_movie = Movie("Star Wars", 5)
your_movie = Movie("Your Name", 4.6)

print(my_movie.id)
print(your_movie.id)




