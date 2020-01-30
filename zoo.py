from animals import Penguin, PaintedDog
from habitats import Habitat

# Create a penguin
bob = Penguin("Bob")
# print(bob)
# bob.run()
# bob.swim()

# Create a painted dog
ralph = PaintedDog("Ralph")

# Create a habitat
seaworld = Habitat("Sea World")
seaworld.add_animal(bob)
seaworld.add_animal(ralph)

for animal in seaworld.animals:
    print(animal)