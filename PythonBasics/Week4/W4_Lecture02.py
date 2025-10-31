# ---------------------------
# 🌀 ITERATION & RECURSION - Part 02
# ---------------------------

# This exercise illustrates Iteration and Recursion, so the countdown function is implemented.
# This function prints a countdown from a given number down to 1, then displays "Liftoff!" at the end.
#
# It can be implemented either iteratively (using loops)
# or recursively (by calling itself until a base case is reached).

# -----------------------------
# 3️⃣ Recursive countdown
# -----------------------------
# Recursive implementation using function calls.
# The function calls itself with a decremented value until it reaches the base case.
# When the base case is reached, the recursion unwinds.
# Here, the base case is when n <= 0.
# Each recursive call progresses toward this base case by decrementing n.
# When n reaches 0, the function prints "Liftoff!" and the recursion ends.
# 💡 NOTE: This example demonstrates how recursion can achieve the same effect as iteration.

def countdown_rec(n: int) -> None:
    """
    Prints: n, n-1, ..., 1, then 'Liftoff!' using recursion.
    Precondition: n >= 0
    """
    # Base case (termination condition):
    # When n <= 0, stop making recursive calls.
    if n <= 0:
        print("Liftoff!")  # runs exactly once, at the end
        return

    # Work for this call frame:
    print(n)

    # Recursive step: call the same function with a smaller input (n - 1),
    # ensuring strict progress toward the base case so recursion terminates.
    countdown_rec(n - 1)

# Example usage:
# countdown_rec(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# -----------------------------
# 💡 NOTE: (inside comments)
# -----------------------------
# - Anything you can write with iteration, you can also write with recursion (and vice versa).
# - Time complexity: O(n) for all versions above.
# - Space complexity:
#     * Iterative: O(1) (loop variables only).
#     * Recursive: O(n) due to call stack depth.
# - Recursion can be less efficient due to function call overhead.
# - Use recursion when it leads to clearer, more maintainable code, especially for problems naturally defined recursively.
# - Be cautious of hitting recursion limits for deep recursions; Python's default limit is 1000.
# -----------------------------