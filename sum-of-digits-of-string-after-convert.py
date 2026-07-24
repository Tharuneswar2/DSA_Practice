# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def getSum(s: str) -> int:
    # Initialize sum variable to store the sum of digits
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Add the integer value of the digit to the total sum
            total_sum += int(char)
    
    # Return the total sum
    return total_sum