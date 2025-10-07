# ---------------------------
# Strings
# ---------------------------

a = "Hello"
b = "World"

# Concatenation
print(a + " " + b)     # "Hello World"

# Repetition
print(a * 3)           # "HelloHelloHello"

# Lexicographic comparison
print("apple" > "banana")   # False
print("zebra" > "apple")    # True


# ---------------------------
# Type Casting
# ---------------------------

c = 10        # int
d = 11.5      # float

# Automatic casting (int promoted to float)
print(c + d)            # 21.5

# Static casting (explicit conversion)
print(c + int(d))       # 21   (11.5 → 11)
print(str(c))           # "10"
print(float(c))         # 10.0
print(bool(c))          # True (non-zero → True)


# ---------------------------
# Booleans
# ---------------------------

val = True
val1 = False

# Boolean as integers
print(int(val))     # 1
print(int(val1))    # 0
print(True + True)  # 2

# Logical operators
print(val and val1)   # False
print(val or val1)    # True
print(not val1)       # True

# Comparison (since True=1, False=0)
print(val > val1)     # True  (1 > 0)
print(val == 1)       # True
print(val1 == 0)      # True