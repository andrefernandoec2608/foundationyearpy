# -----------------------------------
# 🌀 SELF PARAMETER
# -----------------------------------

# 'self' is the reference to the current object
# You never pass it manually when calling a method — Python does it for you.
# Instance methods always have 'self' as the first parameter

class Student:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hi, I'm {self.name}!")

s1 = Student("Luna") # Create an instance of Student, Python passes 'self' automatically
s1.say_hello()

"""
💡NOTE: Equivalent manual call (rarely used but valid).
Python internally calls: Student.say_hello(s1)
Student.say_hello(s1)
"""