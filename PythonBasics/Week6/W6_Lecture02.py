# ---------------------------
# 🌀 WEEK 6 — MODULE 1 SCRIPT
# Non-Scalar Objects & Aliasing/Copies (List, Dict, Tuple)
# All explanations are inside comments; run top-to-bottom.
# ---------------------------

# ======================================================
# 0) VALUE vs REFERENCE (quick mental model)
# ======================================================
# In Python, variables hold REFERENCES to objects in memory.
# Mutating a mutable object changes it "in place" (same identity).
# Rebinding a variable points the name to a NEW object.

x = 5
y = x          # both reference the same int object 5
y += 1         # ints are immutable → creates NEW int (6), y now points to 6
assert x == 5 and y == 6

# ======================================================
# 1) LIST — ordered, mutable sequence
# ======================================================
fruits = ["apple", "banana", "cherry"]

# Access & mutate
assert fruits[0] == "apple"
fruits[1] = "orange"                 # in-place mutation
fruits.append("grape")               # add at end
fruits.remove("orange")              # remove by value
assert fruits == ["apple", "cherry", "grape"]

# Common patterns
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]   # comprehension
evens = list(filter(lambda n: n % 2 == 0, numbers))
assert squares == [1, 4, 9, 16] and evens == [2, 4]

# ======================================================
# 2) DICTIONARY — mapping of key → value, mutable
# ======================================================
person = {"name": "Alice", "age": 30}

# Access, add/update, delete
assert person["name"] == "Alice"
person["age"] = 31                   # update
person["city"] = "Budapest"          # add
del person["city"]                   # delete
assert person == {"name": "Alice", "age": 31}

# KEYS MUST BE IMMUTABLE (hashable): str, int, bool, tuple-of-immutables, etc.
valid_keys = {
    "key": "string is ok",
    42: "int is ok",
    (1, 2): "tuple is ok if its contents are immutable",
    True: "bool is ok",
}

# INVALID (uncommenting these would raise TypeError: unhashable type)
# bad = { [1, 2]: "list is mutable → not hashable" }
# bad2 = { {"a": 1}: "dict is mutable → not hashable" }

# ======================================================
# 3) TUPLE — ordered, immutable sequence
# ======================================================
coords = (10, 20, 30)
assert coords[1] == 20

# coords[1] = 99  # ❌ TypeError: 'tuple' object does not support item assignment

# Create a new tuple instead (original remains unchanged)
new_coords = coords + (40,)
assert new_coords == (10, 20, 30, 40) and coords == (10, 20, 30)

# IMPORTANT: a tuple can contain MUTABLE objects; the tuple stays immutable
nested = (["a", "b"], 2)
nested[0].append("c")   # mutating the inner list, not the tuple container itself
assert nested == (["a", "b", "c"], 2)

# ======================================================
# 4) EQUALITY vs IDENTITY
# ======================================================
a = [1, 2, 3]
b = a            # alias: b is the same object as a
c = [1, 2, 3]    # equal in value, different object

assert (a == b) and (a is b)          # same value AND same identity
assert (a == c) and (a is not c)      # same value, different identity

# ======================================================
# 5) ALIASING — same object, multiple names
# ======================================================
nums = [1, 2]
alias = nums                # aliasing: both reference the same list
alias.append(3)             # in-place change through alias
assert nums == [1, 2, 3]    # reflects through both names
assert alias is nums        # identity is the same

# ======================================================
# 6) COPIES — shallow vs deep
# ======================================================
import copy

# Shallow copy: duplicates the outer container, reuses references of inner items
outer = [[1], [2]]
shallow = list(outer)       # equivalent to outer.copy() or outer[:]
outer[0].append(99)

assert outer == [[1, 99], [2]]
assert shallow == [[1, 99], [2]]   # inner list shared → change is visible in the shallow copy

# Deep copy: recursively duplicates inner structures
outer2 = [[1], [2]]
deep = copy.deepcopy(outer2)
outer2[0].append(77)

assert outer2 == [[1, 77], [2]]
assert deep   == [[1], [2]]        # independent copy

# ======================================================
# 7) COMMON GOTCHA — list multiplication
# ======================================================
# This creates TWO references to the SAME inner list → aliasing inside
bad = [[0] * 3] * 2     # [[0,0,0], [0,0,0]] but both rows share identity
bad[0][0] = 1
assert bad == [[1, 0, 0], [1, 0, 0]]  # both rows changed unexpectedly

# Correct: build independent rows with a comprehension
ok = [[0] * 3 for _ in range(2)]
ok[0][0] = 1
assert ok == [[1, 0, 0], [0, 0, 0]]

# ======================================================
# 8) MINI PRACTICE (sanity checks)
# ======================================================
# 8.1 Lists mutate in place; tuples do not:
lst = [1, 2, 3]
tpl = (1, 2, 3)
lst.append(4)
assert lst == [1, 2, 3, 4] and tpl == (1, 2, 3)

# 8.2 Dict keys are immutable (hashable):
d = {"a": 1, 2: "two", (3, 4): "tuple-key"}
assert d["a"] == 1 and d[2] == "two" and d[(3, 4)] == "tuple-key"

# 8.3 Aliasing vs copies:
orig = [{"x": 1}, {"y": 2}]
alias2 = orig                 # alias
shallow2 = orig.copy()        # shallow copy
deep2 = copy.deepcopy(orig)   # deep copy

orig[0]["x"] = 999
assert alias2[0]["x"] == 999          # same object
assert shallow2[0]["x"] == 999        # inner dict shared
assert deep2[0]["x"] == 1             # fully independent

# If all asserts pass silently, you have the essentials of:
# - Non-scalar objects (list/dict/tuple)
# - Immutable dict keys
# - Equality vs identity
# - Aliasing vs shallow vs deep copy
# - Common pitfalls (list multiplication)
