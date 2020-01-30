from animals import Penguin
from habitats import Habitat

# Create a penguin
bob = Penguin("Bob")
print(bob)
bob.run()
bob.swim()

# Create a habitat
seaworld = Habitat("Sea World")
seaworld.add_animal(bob)

for animal in seaworld.animals:
    print(animal)