# ---------------------------
# 🌀 CLASS vs INSTANCE ATTRIBUTES
# ---------------------------
# This code demonstrates the difference between class attributes and instance attributes in Python.
# Class attributes are shared across all instances of the class,
# while instance attributes are unique to each instance.

# Define a Dog class with both class and instance attributes
# Class attribute: species
# Instance attributes: name, age
class Dog:
    # Class attribute: shared across all instances
    species = "Canine"

    def __init__(self, name, age):
        # Instance attributes: unique per object
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Create instances
d1 = Dog("Fido", 4)
d2 = Dog("Rex", 6)

# Instance attributes
# Each dog has its own name and age
# Print instance attributes
print("Instance attrs:", d1.name, d1.age)  # Fido 4
print("Instance attrs:", d2.name, d2.age)  # Rex 6

# Class attribute is visible through both the class and the instances
# Print class attribute
# Accessing class attribute via class and instances
print("Class attr via class:", Dog.species)  # Canine
print("Class attr via d1:", d1.species)      # Canine
print("Class attr via d2:", d2.species)      # Canine

# Mutate the CLASS attribute via the class
Dog.species = "Mammal"
# All instances reflect the change
# Print updated class attribute
print("After Dog.species change:")
print("Dog.species:", Dog.species)   # Mammal
print("d1.species:", d1.species)     # Mammal
print("d2.species:", d2.species)     # Mammal

# 🌀 EXTRA knowledge: Inspect namespaces
# instance.__dict__: A dictionary used to store an object's attributes.
print("d1.__dict__:", d1.__dict__)   # {'name': 'Fido', 'age': 4}
print("d2.__dict__:", d2.__dict__)   # {'name': 'Rex', 'age': 6}
# class.__dict__: A mappingproxy object that shows the class's namespace.
print(Dog.__dict__) # {'__module__': '__main__', 'species': 'Mammal', '__init__': <function Dog.__init__ at ...>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None} 