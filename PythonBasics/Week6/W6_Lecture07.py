# ---------------------------
# 🌀 ENCAPSULATION (Property, Setter & Deleter)
# ---------------------------
# Demonstrate @property, @setter, and @deleter

class Config:
    def __init__(self):
        self.__token = "ABC123"

    # @property turns this method into a readable attribute
    @property
    def token(self):
        return self.__token

    # @token.setter controls how the value is changed
    @token.setter
    def token(self, value):
        # this setter — validates and updates the atribute
        if not isinstance(value, str):
            raise ValueError("Token must be a string")
        self.__token = value

    # @token.deleter defines what happens when using 'del obj.token'
    @token.deleter
    def token(self):
        # Deleter — custom cleanup or revoke logic.
        print("Token deleted (revoked)")
        self.__token = None

# ---------------------------
# Usage
# ---------------------------
cfg = Config()

# Read using @property (no parentheses)
print(cfg.token)       # ABC123

# Update using @setter
cfg.token = "XYZ999"
print(cfg.token)       # XYZ999

# Delete using @deleter
del cfg.token          # "Token deleted (revoked)"
print(cfg.token)       # None

"""
⚠️ ALERT: If we remove @property from def token(self): we must use parentheses:
cfg.token() instead of cfg.token
It would become a normal method, not an attribute getter.
"""