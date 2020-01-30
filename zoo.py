from animals import Penguin, PaintedDog
from habitats import Habitat, Aquarium

# Create a penguin
bob = Penguin("Bob")
# print(bob)
# bob.run()
# bob.swim()

# Create a painted dog
ralph = PaintedDog("Ralph")

# Create a habitat
seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)
seaworld.add_swimmer_type_check(ralph)

for animal in seaworld.animals:
    print(animal)