# ---------------------------
# 🌀 INHERITANCE (Parent & Child Classes)
# ---------------------------
# Example: Pizza 🍕 (parent) → PineapplePizza 🍍🍕 (child)
# Focus on overriding methods (bake & serve) + using super()

# -----------------------------------
# Parent class
# -----------------------------------
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def bake(self):
        print(f"Baking a pizza with {', '.join(self.ingredients)}... 🍕")

    def serve(self):
        print("Serving the pizza hot and crispy! 🔥")


# -----------------------------------
# Child class (inherits from Pizza)
# -----------------------------------
class PineapplePizza(Pizza):
    def __init__(self, ingredients):
        # Call the parent constructor to initialize shared attributes
        super().__init__(ingredients)
        self.has_pineapple = True

    # Override the parent bake() method
    def bake(self):
        # Call the parent version first
        super().bake()
        print("Adding pineapple chunks on top 🍍 (controversial choice!)")

    # Override the serve() method too
    def serve(self):
        # Call the parent's serve method
        super().serve()
        print("Warning: This pizza may trigger strong opinions! 😂")

    # Add a new method exclusive to the child class
    def defend_choice(self):
        print("Pineapple on pizza is art — don’t judge me! 😎")


# -----------------------------------
# Usage examples
# -----------------------------------
classic = Pizza(["cheese", "tomato"])
hawaiian = PineapplePizza(["cheese", "tomato", "ham"])

print("--- Parent class ---")
classic.bake()
classic.serve()

print("\n--- Child class ---")
hawaiian.bake()           # Overrides bake()
hawaiian.serve()          # Overrides serve()
hawaiian.defend_choice()  # Unique method