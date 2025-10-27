# ---------------------------
# 🌀 ITERATION & RECURSION SUMMARY
# ---------------------------

# This exercise illustrates Iteration and Recursion, so the countdown function is implemented.
# This function prints a countdown from a given number down to 1, then displays "Liftoff!" at the end.
#
# It can be implemented either iteratively (using loops)
# or recursively (by calling itself until a base case is reached).

# -----------------------------
# 1️⃣ Iterative countdown with a WHILE loop
# -----------------------------
def countdown_iter(n: int) -> None:
    """
    Prints: n, n-1, ..., 1, then 'Liftoff!'.
    Precondition: n >= 0
    """
    # Loop as long as the condition n > 0 holds.
    # Termination condition: when n == 0, (n > 0) becomes False and the loop ends.
    while n > 0:
        print(n)    # do the work for this iteration
        n -= 1      # progress toward termination

    print("Liftoff!")

# Example usage:
# countdown_iter(3)
# Output:
# 3
# 2
# 1
# Liftoff!


# -----------------------------
# 2️⃣ Iterative countdown with a FOR loop
# -----------------------------
def countdown_for(n: int) -> None:
    """
    Same behavior using a for-loop (descending range).
    Precondition: n >= 0
    """
    # range(start, stop, step); stop is exclusive.
    # Here we go from n down to 1 (inclusive) by -1.
    for i in range(n, 0, -1):
        print(i)

    # When the iterator is exhausted, the loop ends automatically.
    print("Liftoff!")

# Example usage:
# countdown_for(4)
# Output:
# 4
# 3
# 2
# 1
# Liftoff!


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