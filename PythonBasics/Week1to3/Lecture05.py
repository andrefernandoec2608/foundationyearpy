# ---------------------------
# 🌀 FLOW CONTROL & LOOPS SUMMARY
# ---------------------------

# ---------- IF / ELIF / ELSE ----------
x = 5

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")


# ---------- WHILE LOOP ----------
# Repeats while the condition is True
count = 0
while count < 3:
    print("Count =", count)
    count += 1
print("While loop finished")


# ---------- FOR LOOP with range() ----------
# range(stop) → 0, 1, 2, ..., stop-1
# range(start, stop, step)
for i in range(5):
    print("i =", i)

print("---- Range with start/stop/step ----")
for i in range(1, 10, 3):
    print("i =", i)   # 1, 4, 7


# ---------- FOR LOOP with enumerate() ----------
# Useful to get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)


# ---------- CONTINUE ----------
# Skips the rest of the current iteration
for i in range(5):
    if i == 2:
        continue  # Skip printing 2
    print("continue example ->", i)

# Output: 0, 1, 3, 4


# ---------- BREAK ----------
# Exits the loop completely
for i in range(5):
    if i == 3:
        break  # Stop loop when i == 3
    print("break example ->", i)

# Output: 0, 1, 2


# ---------- PASS ----------
# Does nothing; used as a placeholder (TODO)
for i in range(5):
    if i == 2:
        pass  # TODO: Implement some logic later
    else:
        print("pass example ->", i)

# Output: 0, 1, 2, 3, 4  (pass does nothing)