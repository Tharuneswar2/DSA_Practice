# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def removeDigit(number: str, digit: str) -> str:
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a flag to track if the digit is found and removed
    found = False
    
    # Iterate over each character in the number string
    for char in number:
        # If the character matches the digit and it's not found yet
        if char == digit and not found:
            # Set the found flag to True
            found = True
            # Continue to the next iteration without adding the digit to the result
            continue
        # Add the character to the result string
        result += char
    
    # If the digit is not found in the number, remove the last digit
    if not found:
        result = result[:-1]
    
    # Return the result
    return result