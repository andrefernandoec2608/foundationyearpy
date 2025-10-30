# ---------------------------
# 🌀 FILE HANDLING & 'WITH' STATEMENT USAGE
# ---------------------------

# -----------------------------
# 1️⃣ FILE HANDLING BASICS
# -----------------------------
# open(filename, mode)
# Modes: "r" (read), "w" (write), "a" (append), "r+" (read/write)

# OPEN a file (creates if not exists in "w"/"a" modes)
# WRITE ("w") → overwrites existing content
f = open("demo.txt", "w")
f.write("Line 1\nLine 2\n")
f.close()

# APPEND ("a") → adds to end of file
f = open("demo.txt", "a")
f.write("Line 3 (appended)\n")
f.close()

# READ ("r") → read whole content
f = open("demo.txt", "r")
print(f.read())  # Shows Line 1/Line 2/Line 3
f.close()

# POINTER METHODS
# f.tell() → current position
# f.seek(offset, whence) → move pointer (0=start, 1=current, 2=end)
f = open("demo.txt", "r+")
print("=== POINTER DEMO ===")
print("pos:", f.tell())             # pos: 0
chunk = f.read(5)                   # read first 5 chars
print("first5:", chunk)             # e.g., 'Line '
print("pos:", f.tell())             # e.g., 5
f.seek(0)                           # go to start
f.write("#####")                    # overwrite first 5 chars
f.seek(0)
print(f.read())                     # file with '#####' at the start
f.close()

# ITERATING LINES (file objects are iterables)
# for line in f:
print("=== ITERATE LINES ===")
with open("demo.txt", "r") as f:
    for line in f:
        print(line.rstrip())        # Prints each line without trailing '\n'

# -----------------------------
# 2️⃣ 'WITH' STATEMENT USAGE
# -----------------------------
# The 'with' statement automatically manages resources (like files, connections, etc.)
# It ensures that the file is properly CLOSED after the block finishes,
# even if an error occurs inside the block.
# This behavior is provided by the Context Manager protocol (__enter__ / __exit__ methods).

# open("quick.txt", "w") → opens/creates a file for writing ('w' = write mode)
# as f → assigns the opened file object to variable 'f'
with open("quick.txt", "w") as f:
    f.write("Hello (auto-closed)")
    # No need to call f.close() manually!

# After leaving the 'with' block, Python automatically calls f.close()
print("quick.txt written (file is auto-closed).")

"""
💡 NOTE: Why 'WITH' STATEMENT is preferred:
- Cleaner syntax (no need for try/finally or manual close)
- Prevents resource leaks
- Commonly used with: files, sockets, database connections, locks, etc.
"""

# SIMPLE FILE DELETES: Clean up created files
import os
os.remove("demo.txt")
os.remove("quick.txt")
print("Files deleted ✅")