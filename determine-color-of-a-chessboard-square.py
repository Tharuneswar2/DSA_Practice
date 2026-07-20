# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def squareIsWhite(coordinates: str) -> bool:
    # Convert the given coordinates to a standard format (a-h, 1-8) for easier calculation
    x = ord(coordinates[0]) - ord('a')  # Convert the letter to its corresponding number (a=0, b=1, ..., h=7)
    y = int(coordinates[1]) - 1  # Convert the number to its corresponding row (1=0, 2=1, ..., 8=7)

    # Calculate the sum of the x and y coordinates
    total = x + y

    # If the total is even, the square is black; otherwise, it's white
    return total % 2 != 0