# ---------------------------
# 🌀 STRING QUOTES & ESCAPE CHARACTERS SUMMARY
# ---------------------------

# 1️⃣ Newline (\n)
# Starts a new line
print("Hello\nWorld")
# Output:
# Hello
# World


# 2️⃣ Tab (\t)
# Adds a horizontal tab (like multiple spaces)
print("Name\tAge\tCountry")
print("Alice\t25\tHungary")
# Output:
# Name    Age     Country
# Alice   25      Hungary


# 3️⃣ Double quotes inside double quotes (\" )
print("She said, \"Python is awesome!\"")
# Output: She said, "Python is awesome!"


# 4️⃣ Backslash (\\)
print("This is a backslash: \\")
# Output: This is a backslash: \


# ---------------------------
# 🌀 SINGLE, DOUBLE, AND TRIPLE QUOTES
# ---------------------------

# 5️⃣ Single quotes (' ')
single_quote = 'Hello Python'
print(single_quote)

# 6️⃣ Double quotes (" ")
double_quote = "Hello Python"
print(double_quote)

# Both are identical
print(single_quote == double_quote)  # True


# 7️⃣ When to use each
# Use double quotes if your text contains a single quote
sentence_1 = "It's a beautiful day!"
print(sentence_1)  # Works fine

# Use single quotes if your text contains double quotes
sentence_2 = 'She said, "Python is awesome!"'
print(sentence_2)


# 8️⃣ If your text contains both → use escape (\)
sentence_3 = "She said, \"It's Python time!\""
print(sentence_3)


# 9️⃣ Triple quotes for multi-line strings
paragraph = """She said, "It's a beautiful day!"
Let's go coding in Python."""
print(paragraph)
# Output:
# She said, "It's a beautiful day!"
# Let's go coding in Python.

# 🔟 RAW STRINGS (r"")
# Prevents escape sequences from being processed
path = r"C:\Users\Gerardo\Documents"
print(path)
# Output: C:\Users\Gerardo\Documents