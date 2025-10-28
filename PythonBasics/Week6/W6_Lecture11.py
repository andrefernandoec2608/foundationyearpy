# ---------------------------
# 🌀 OPERATOR OVERLOADING 
# ---------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overloading: defines how '+' operator works
    def __add__(self, other):
        # ✅ Good practice #1 — type checking
        if not isinstance(other, Vector):
            # Return NotImplemented if the operation is not supported for this type
            # This tells Python to try the reverse operation
            return NotImplemented

        # ✅ Good practice #2 — return a NEW object, don't modify the originals
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __repr__(self):
        # Developer-friendly representation for print()
        return f"Vector({self.x}, {self.y})"

# -----------------------------------
# Usage examples
# -----------------------------------
v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2  # Internally calls v1.__add__(v2)

print(v3)  # Vector(6, 4)

# -----------------------------------
# Demonstrating NotImplemented
# -----------------------------------
result = v1 + 5
print(result)
"""
⚠️ ALERT: TypeError: unsupported operand type(s) so __add__ returned NotImplemented
"""

"""
🌀 EXTRA knowledge: Common Operator Methods in Python

| Operator | Method name         | Example usage | Equivalent call         |
|-----------|--------------------|----------------|------------------------|
| +         | __add__            | a + b          | a.__add__(b)           |
| -         | __sub__            | a - b          | a.__sub__(b)           |
| *         | __mul__            | a * b          | a.__mul__(b)           |
| /         | __truediv__        | a / b          | a.__truediv__(b)       |
| //        | __floordiv__       | a // b         | a.__floordiv__(b)      |
| %         | __mod__            | a % b          | a.__mod__(b)           |
| **        | __pow__            | a ** b         | a.__pow__(b)           |
| <         | __lt__             | a < b          | a.__lt__(b)            |
| <=        | __le__             | a <= b         | a.__le__(b)            |
| >         | __gt__             | a > b          | a.__gt__(b)            |
| >=        | __ge__             | a >= b         | a.__ge__(b)            |
| ==        | __eq__             | a == b         | a.__eq__(b)            |
| !=        | __ne__             | a != b         | a.__ne__(b)            |
"""