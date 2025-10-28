# ---------------------------
# 🌀 OBJECT REPRESENTATION (__str__ & __repr__)
# ---------------------------
# __str__  -> user-friendly representation (for humans)
# __repr__ -> technical representation (for developers)

# -----------------------------------
# 1️⃣ DEFAULT REPRESENTATION
# -----------------------------------
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Luna")

print(p)
print(repr(p))
# 👉 Both outputs should be like: <__main__.Person object at 0x000001A5B...>
# This is the default: class name + memory address (it is not readable).

# -----------------------------------
# 2️⃣ ADDING __str__ (HUMAN-FRIENDLY)
# -----------------------------------
# __str__ is called by print(obj) or str(obj)
# It should return a string that is clear and readable for users.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # "Nice" representation for humans
        return f"{self.name}, {self.age} years old"

p = Person("Luna", 22)

print(p)          # Luna, 22 years old
print(str(p))     # Luna, 22 years old

# -----------------------------------
# 3️⃣ ADDING __repr__ (DEVELOPER-FRIENDLY)
# -----------------------------------
# __repr__ is called by repr(obj) or by the interactive console.
# It should return an unambiguous string, ideally one that could recreate the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Luna", 22)

print(repr(p))    # Person(name='Luna', age=22)
# It is a technical representation for developers

# -----------------------------------
# 4️⃣ DEFINING BOTH __str__ AND __repr__
# -----------------------------------
# If both exist:
#   print(obj) → calls __str__
#   repr(obj) or the console → calls __repr__

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} (Grade: {self.grade})"  # readable for users

    def __repr__(self):
        return f"Student(name='{self.name}', grade='{self.grade}')"  # technical

s = Student("Kai", "A")

print(s)         # Kai (Grade: A)
print(repr(s))   # Student(name='Kai', grade='A')

# -----------------------------------
# 5️⃣ FALLBACK BEHAVIOR
# -----------------------------------
# If __str__ is NOT defined, Python uses __repr__ as a fallback.

class Animal:
    def __init__(self, species):
        self.species = species

    def __repr__(self):
        return f"Animal(species='{self.species}')"

a = Animal("Cat")
print(repr(a))   # Animal(species='Cat')
print(a)         # Uses __repr__ because __str__ is missing