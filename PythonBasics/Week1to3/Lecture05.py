# ---------------------------
# 🌀 FLOW CONTROL & LOOPS
# ---------------------------

# 1️⃣ IF / ELIF / ELSE
print("\n\n🚀 IF / ELIF / ELSE")
x = 5

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")


# 2️⃣ WHILE LOOP 
print("\n\n🚀 WHILE LOOP")
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


# 3️⃣ FOR LOOP with enumerate()
print("\n\n🚀 FOR LOOP with enumerate()")
# Useful to get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# 4️⃣ CONTINUE 
print("\n\n🚀 CONTINUE")
# Skips the rest of the current iteration
for i in range(5):
    if i == 2:
        continue  # Skip printing 2
    print("continue example ->", i)

# Output: 0, 1, 3, 4


# 5️⃣ BREAK
print("\n\n🚀 BREAK")
# Exits the loop completely
for i in range(5):
    if i == 3:
        break  # Stop loop when i == 3
    print("break example ->", i)

# Output: 0, 1, 2


# 6️⃣ PASS ** ⚠️ IMPORTANTE ALERT: It helps to keep Python syntax **
print("\n\n🚀 PASS")
# Does nothing; used as a placeholder
for i in range(5):
    if i == 2:
        pass  # Placeholder, does nothing
    else:
        print("pass example ->", i)

# Output: 0, 1, 3, 4  (pass does nothing)