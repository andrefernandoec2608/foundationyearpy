# ---------------------------
#  🌀 FUNCTION PARAMETERS & ARGUMENTS SUMMARY
# ---------------------------

# 1️⃣ POSITIONAL ARGUMENTS
# Arguments are passed in the same order as parameters.
def add(a, b):
    return a + b

print("Positional arguments:", add(3, 5))  # a=3, b=5


# 2️⃣ KEYWORD ARGUMENTS
# You can specify the parameter name explicitly (order doesn't matter).
def greet(name, country):
    print(f"Hello {name} from {country}!")

greet(name="Alice", country="Hungary")
greet(country="Spain", name="Bob")


# 3️⃣ DEFAULT PARAMETERS
# Parameters can have default values.
def greet_default(name, country="Hungary"):
    print(f"Hello {name} from {country}!")

greet_default("Alice")          # Uses default -> Hungary
greet_default("Bob", "Spain")   # Overrides default


# 4️⃣ ARBITRARY POSITIONAL ARGUMENTS (*args)
# *args collects extra positional arguments into a tuple.
def add_all(*args):
    print("Args received:", args)
    return sum(args)

print("Sum of all:", add_all(1, 2, 3))
print("Sum of all:", add_all(5, 10, 15, 20))


# 5️⃣ ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# **kwargs collects keyword arguments into a dictionary.
def show_info(**kwargs):
    print("Keyword arguments received:", kwargs)

show_info(name="Alice", age=25, country="Hungary")