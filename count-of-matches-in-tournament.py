def numberOfMatches(n: int) -> int:
    # In a tournament, the number of matches is equal to the number of teams minus one
    # This is because each match eliminates one team, and the tournament continues until only one team is left
    # So, we can simply return n - 1
    return n - 1

# Alternatively, we can use a mathematical formula to calculate the number of matches
def numberOfMatchesMath(n: int) -> int:
    # The number of matches is equal to the number of teams minus one, which can be calculated using the formula n - 1
    # However, we can also use the formula n * (n - 1) / 2 to calculate the number of matches
    # This formula is derived from the fact that each team plays every other team once, and each match is counted twice
    # So, we can return the result of this formula
    return n * (n - 1) // 2

# However, the above formula is not necessary for this problem, as the number of matches is simply n - 1
# So, we can stick with the first solution