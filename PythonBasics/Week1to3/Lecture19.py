# ---------------------------
# 🌀 INPUT() SUMMARY
# ---------------------------

# 1️⃣ Basic input
# input() reads user input from the console and always returns a STRING (str)
name = input("Enter your name: ")
print(f"Hello, {name}!")   # f-string to include variable in text


# 2️⃣ Checking input type
# Even if the user enters a number, input() still returns a string
value = input("Enter any value: ")
print("You entered:", value)
print("Type of input:", type(value))  # <class 'str'>


# 3️⃣ Type casting (conversion)
# Convert string input into a number if you want to do math operations

# Convert to integer
num1 = int(input("Enter an integer: "))
print("Type after int():", type(num1))

# Convert to float
num2 = float(input("Enter a floating-point number: "))
print("Type after float():", type(num2))

# Basic arithmetic with inputs
print(f"Sum: {num1 + num2}")