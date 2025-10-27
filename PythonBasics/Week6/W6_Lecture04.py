# ---------------------------
# 🌀 CLASS vs INSTANCE ATTRIBUTES
# ---------------------------
# This code demonstrates the difference between class attributes and instance attributes in Python.

class Dog:
    # Class attribute: shared across all instances
    species = "Canine"

    def __init__(self, name, age):
        # Instance attributes: unique per object
        self.name = name
        self.age = age

# Create instances
d1 = Dog("Fido", 4)
d2 = Dog("Rex", 6)

# --- Instance attributes ---
print("Instance attrs:", d1.name, d1.age)  # Fido 4
print("Instance attrs:", d2.name, d2.age)  # Rex 6

# Class attribute is visible through both the class and the instances
print("Class attr via class:", Dog.species)  # Canine
print("Class attr via d1:", d1.species)      # Canine
print("Class attr via d2:", d2.species)      # Canine

# --- Mutate the CLASS attribute via the class ---
Dog.species = "Mammal"
print("After Dog.species change:")
print("Dog.species:", Dog.species)   # Mammal
print("d1.species:", d1.species)     # Mammal
print("d2.species:", d2.species)     # Mammal

# 🌀 EXTRA knowledge: Inspect namespaces
# Class namespace holds instance attributes and methods:
print("d1.__dict__:", d1.__dict__)   # {'name': 'Fido', 'age': 4}
print("d2.__dict__:", d2.__dict__)   # {'name': 'Rex', 'age': 6}
# Class namespace holds class attributes and methods:
print(Dog.__dict__)