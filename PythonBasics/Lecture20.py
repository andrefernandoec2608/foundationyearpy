# ---------------------------
# INTEGER DIVISION (//) AND MODULUS (%) SUMMARY
# ---------------------------

# 1️⃣ Basic idea
# //  → integer division (keeps only the whole part)
# %   → modulus (keeps only the remainder)

a = 123
b = 10

print("a =", a)
print("b =", b)
print("a // b =", a // b)   # 123 // 10 → 12 (integer part)
print("a % b  =", a % b)    # 123 % 10  → 3  (remainder)

# Output:
# a // b = 12
# a % b  = 3


# 2️⃣ Combined usage (common digit extraction pattern)
# Use % 10 to get the last digit
# Use // 10 to remove the last digit

number = 9876

while number > 0:
    last_digit = number % 10      # get last digit
    print("Last digit:", last_digit)
    number = number // 10         # remove last digit

# Output:
# Last digit: 6
# Last digit: 7
# Last digit: 8
# Last digit: 9


# 3️⃣ Shorthand operator (//=)
# number //= 10  is the same as  number = number // 10
num = 1234
print("Before:", num)

num //= 10   # equivalent to num = num // 10
print("After one step:", num)

num //= 10
print("After two steps:", num)

# Output:
# Before: 1234
# After one step: 123
# After two steps: 12


# 4️⃣ Example: show integer division and remainder side by side
dividend = 145
divisor = 12

print("\nInteger division:", dividend // divisor)  # 12
print("Remainder:", dividend % divisor)            # 1