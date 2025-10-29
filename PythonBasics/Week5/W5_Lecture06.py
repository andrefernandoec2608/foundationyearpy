# ---------------------------
# 🌀 ENCAPSULATION & ATTRIBUTES AND METHODS
# ---------------------------
# Python handles visibility — public, _protected, and __private for attributes and methods.
# Python does NOT enforce access control like Java or C++.
# Instead, it relies on *naming conventions* — a "gentlemen's agreement" between developers.

class Account:
    def __init__(self, owner, balance):
        # PUBLIC ATTRIBUTE: No underscore means:
        # Anyone can read or modify it from outside the class (fully public)
        self.owner = owner

        # _PROTECTED ATTRIBUTE: A single underscore means:
        # This is for internal use only. You can access it, but you *shouldn't*.
        # It’s not enforced by Python, only a convention between developers.
        self._status = "active"

        # __PRIVATE ATTRIBUTE
        # A double underscore triggers *name mangling*:
        # Python internally renames it to _Account__balance.
        # This hides it from casual access and prevents name conflicts in subclasses.
        # However, it can still be accessed via its mangled name (_Account__show_balance)
        self.__balance = balance

    # PUBLIC METHOD
    # Same logic as a public attribute.
    def show_owner(self):
        print("It's a public method.")

    # _PROTECTED METHOD (by convention)
    # Same logic as a protected attribute.
    def _show_status(self):
        print("It's a protected method.")

    # __PRIVATE" METHOD
    # Same logic as a private attribute.
    def __show_balance(self):
        print("It's a private method.")

# Create an instance
acc = Account("Luna", 1000)

# --- Public attribute ---
print(acc.owner)        # Luna
acc.show_owner()        # Owner: Luna

# --- Protected attribute ---
print(acc._status)      # ⚠️ accessible but intended for internal use
acc._show_status()      # Status: active

# --- Private attribute ---
# print(acc.__balance)  # ❌ AttributeError (Python hides it via name mangling)
print(acc._Account__balance)  # Accessed manually through mangled name

# --- Private method ---
# acc.__show_balance()  # ❌ AttributeError
acc._Account__show_balance()  # Accessed manually through mangled name