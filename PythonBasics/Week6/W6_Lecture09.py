# ---------------------------
# 🌀 BOUND vs UNBOUND METHODS
# ---------------------------
# Here, we explore the difference between bound and unbound methods in Python.
# This is crucial for understanding how instance methods work in classes.
# We will see how Python automatically passes the instance (self) when calling methods
# from an instance, and how we need to pass it manually when calling methods from the class itself.
# -----------------------------------

class Student:
    def say_hello(self):
        print(f"Hello! I am {self}")

# Create an instance
s1 = Student()

# -----------------------------------
# 🔹 Bound Method
# -----------------------------------
# When you call a method from an instance (s1.say_hello()),
# Python automatically passes the instance as the first argument (self).
s1.say_hello()               # ✅ Automatic and preferred

# -----------------------------------
# 🔹 Unbound Method
# -----------------------------------
# When you call the method directly from the class (Student.say_hello),
# You MUST pass the instance manually.
Student.say_hello(s1)        # ✅ Manual but same result

# -----------------------------------
# 📊 Quick Comparison
# -----------------------------------
# | Type of call     | Example                | What happens internally            | 'self' passed automatically |
# |------------------|------------------------|------------------------------------|-----------------------------|
# | Bound method     | s1.say_hello()         | Student.say_hello(s1)              | ✅ Yes                      |
# | Unbound method   | Student.say_hello(s1)  | You pass s1 manually               | ❌ No                       |

# -----------------------------------
# 🔍 Inspecting the difference
# -----------------------------------
print(s1.say_hello)          # <bound method Student.say_hello of <__main__.Student object at ...>>
print(Student.say_hello)     # <function Student.say_hello at ...>