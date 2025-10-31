# ---------------------------
# BUILTIN, THIRD-PARTY & CUSTOM MODULES 
# ---------------------------
# This script demonstrates how to use built-in, third-party,
# and custom modules in Python.
#
# A module is simply a .py file that contains Python code, including functions, classes and variables.
# This allows you to divide your code into logical, reusable sections.

"""
💡 NOTE: Python modules come from three main sources:
 1) Built-in modules (standard library) → already included with Python.
    Examples: math, os, sys, datetime, random.
 2) Third-party modules→ installed via pip (community-created).
    Examples: requests, pandas, numpy, matplotlib.
 3) Custom modules→ your own .py files you import.
"""

""""
💡 NOTE:
Functions like print(), len(), range(), list, dict, etc. belong to the built-in namespace,
not to the built-in modules — they are always available without import.
"""

# 1️⃣ IMPORT STYLES
# Different ways to import modules and their contents.
import math
print(math.sqrt(16))        # import the whole module

from math import sqrt
print(sqrt(25))             # import a specific name

from math import sqrt as s
print(s(9))                 # alias for convenience

# Multiple imports
from math import factorial, log
print(factorial(5))
print(round(log(8, 2), 2)) 

# ======================================================
# 2️⃣ BUILT-IN MODULES
# ======================================================
import os
print(os.getcwd())          # current working directory (path string)

from datetime import date, datetime
today = date.today()
now = datetime.now()
print("Today:", today)
print("Now:", now)

import random
print(random.randint(1, 6)) 
print(random.choice(['red', 'green', 'blue']))

# Tip: sys is useful for interpreter info and paths
import sys
print(sys.version.split()[0])  # Python version (e.g., '3.12.3')
# print(sys.path)              # search paths used by the import machinery

# ======================================================
# 3️⃣ THIRD-PARTY MODULES (COMMENTED — DIDACTIC ONLY)
# ======================================================
"""
# Install with pip (terminal):
#   pip install requests

# Then in Python:
import requests
res = requests.get("https://api.github.com")
print(res.status_code)      # 200
"""

# 4️⃣ CUSTOM MODULE — YOUR OWN .py FILE
#   mylibraryexample.py is already created in the same folder as this script.
#   mylibraryexample.py has a 'def greet(name: str) -> str:' method implemented.
import w6mylibraryexample as mylib
print(mylib.greet("Classmate"))

"""
💡 NOTE: Python automatically creates a "__pycache__" folder when you run or import modules.
It stores compiled bytecode (.pyc files) to speed up future executions.
You can safely delete it — Python will recreate it when needed.
"""