# ---------------------------
# 🌀 SHADOWING 
# ---------------------------
# Shadowing means that an instance defines an attribute with the same name as a class attribute,
# hiding (or overriding) the class’s version for that specific object.

class Dog:
    species = "Mammal"   # class attribute (shared default)
    def __init__(self, name):
        self.name = name # instance attribute

d1 = Dog("Fido")
d2 = Dog("Rex")

print("Initial:")
print("Dog.species:", Dog.species)   # Mammal
print("d1.species:", d1.species)     # Mammal (reads from class)
print("d2.species:", d2.species)     # Mammal (reads from class)
print("d1.__dict__:", d1.__dict__)   # {'name': 'Fido'}
print("d2.__dict__:", d2.__dict__)   # {'name': 'Rex'}

# SHADOWING: assign on ONE instance to the SAME NAME as the class attribute
# This creates an INSTANCE attribute that shadows the class attribute for that instance only.
d1.species = "RobotDog"  # d1 instance an attribute that shadows class attribute
print("\nAfter d1 sets species:")
print("Dog.species:", Dog.species)   # Mammal (unchanged)
print("d1.species:", d1.species)     # RobotDog (instance-level)
print("d2.species:", d2.species)     # Mammal (still class-level)
print("d1.__dict__:", d1.__dict__)   # d1 now includes 'species' : {'name': 'Fido', 'species': 'RobotDog'}

# Modify the CLASS attribute afterward
# This does NOT affect d1.species because it is shadowing the class attribute.
# d2.species still reads from the class attribute.
# The class attribute is changed for all instances that do not shadow it.
Dog.species = "Vertebrate"
print("\nAfter changing Dog.species at the class level:")
print("Dog.species:", Dog.species)   # Vertebrate
print("d1.species:", d1.species)     # RobotDog (STILL shadowing class value)
print("d2.species:", d2.species)     # Vertebrate (reads from class)

# Remove the shadow to reveal the class attribute again
# Deleting the instance attribute removes the shadowing effect.
# d1.species now falls back to the class attribute.
# This only affects d1; d2 was never shadowing.

# Remove the instance attribute of d1
del d1.species
print("d1.species:", d1.species)     # Vertebrate (reads from class)

# --- Inspecting where things live ---
print("\nWhere do attributes live?")
print("d1.__dict__:", d1.__dict__)  # after deletion above, no 'species' key (falls back to class)
print("d2.__dict__:", d2.__dict__)  # never had 'species' -> always reads class