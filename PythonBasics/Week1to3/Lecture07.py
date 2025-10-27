# ---------------------------
# 🌀 MULTIPLE RETURN VALUES IN PYTHON
# ---------------------------

# A function can return more than one value.
# Python automatically packs them into a tuple.

def get_person_info():
    name = "Alice"
    age = 25
    country = "Hungary"
    return name, age, country   # returns a tuple automatically


# 1️⃣ Receive all values as one tuple
result = get_person_info()
print("Tuple result:", result) # ('Alice', 25, 'Hungary')
print("Type:", type(result)) # <class 'tuple'>

# 2️⃣ Tuple unpacking
# You can unpack multiple values into separate variables.
name, age, country = get_person_info()

print("Name:", name)
print("Age:", age)
print("Country:", country)

# 3️⃣ You can also ignore values using "_"
name, _, country = get_person_info()
print("Ignoring the middle value ->", name, country)

# 4️⃣ Returning other structures (list, dict)
def get_data_structures():
    numbers = [1, 2, 3]
    student = {"name": "Bob", "grade": 90}
    return numbers, student

nums, info = get_data_structures()
print("Numbers list:", nums)
print("Student dict:", info)