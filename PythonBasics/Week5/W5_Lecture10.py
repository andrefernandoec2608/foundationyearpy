# ---------------------------
# 🌀 EQUALITY & IDENTITY IN CLASSES 
# ---------------------------

# -----------------------------------
# 1️⃣ DEFAULT BEHAVIOR ('==' behaves like 'is' behaves unless you define __eq__)
# -----------------------------------
class StudentDefault:
    def __init__(self, name):
        self.name = name

s1 = StudentDefault("Luna")
s2 = StudentDefault("Luna")
s3 = s1  # s3 references the same object as s1

print(s1 == s2)  # False  -> Because no __eq__ is defined,so it compares memory address by default (same as 'is')
print(s1 == s3)  # True   -> same object reference 
print(s1 is s2)  # False  -> different objects
print(s1 is s3)  # True   -> same object reference

# -----------------------------------
# 2️⃣ CUSTOM EQUALITY - Using __eq__(self, other)
# -----------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # 'other' is the object on the right side of ==
        if not isinstance(other, Student):
            return NotImplemented
        # Compare by value (attributes)
        return (self.name, self.age) == (other.name, other.age)

a = Student("Luna", 22)
b = Student("Luna", 22)
c = Student("Kai", 22)
d = a  # d references the same object as a

print(a == b)  # ✅ True  -> same data
print(a == c)  # ❌ False -> different name

print(a is b)  # ❌ False -> not the same object, although equal by value
print(a is d)  # ✅ True  -> same object reference

"""
💡 NOTE: Importance of NotImplemented:
When objects are not comparable, you should return NotImplemented instead of False.
This gives Python the opportunity to try the reversed comparison (b.__eq__(a)).
"""

# -----------------------------------
# 3️⃣ ADDING __hash__ — so objects can be used in sets/dicts
# -----------------------------------
class StudentHashable:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, StudentHashable):
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)

    def __hash__(self):
        # 🌀 hash must be consistent with equality
        return hash((self.name, self.age))

s1 = StudentHashable("Luna", 22)
s2 = StudentHashable("Luna", 22) # s2 is not added because it’s considered the same element (same value and hash as s1)
s3 = StudentHashable("Kai", 22)

students = {s1, s2, s3}
print(len(students))  # 2 -> There are s1 and s3 only
print(s1 in students) # True
print(s2 in students) # True although s2 is not in the set, it is equal to s1
print(s3 in students) # True 