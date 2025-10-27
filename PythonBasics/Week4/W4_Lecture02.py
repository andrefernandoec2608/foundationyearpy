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
# 🌀 Quick notes (inside comments)
# -----------------------------
# - Anything you can write with iteration, you can also write with recursion (and vice versa).
# - Time complexity: O(n) for all versions above.
# - Space complexity:
#     * Iterative: O(1) (loop variables only).
#     * Recursive: O(n) due to call stack depth.