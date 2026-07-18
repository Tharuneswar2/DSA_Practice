# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def balancedStringSplit(s: str) -> int:
    # Initialize a counter to keep track of the balance between 'L' and 'R'
    balance = 0
    # Initialize a counter to keep track of the number of balanced strings
    count = 0
    # Iterate over each character in the string
    for char in s:
        # If the character is 'L', increment the balance
        if char == 'L':
            balance += 1
        # If the character is 'R', decrement the balance
        else:
            balance -= 1
        # If the balance is zero, it means we have a balanced string, so increment the count
        if balance == 0:
            count += 1
    # Return the total count of balanced strings
    return count