# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def isNumber(s):
    # Remove leading and trailing whitespaces
    s = s.strip()
    
    # Check if the string is empty after removing whitespaces
    if not s:
        return False
    
    # Initialize flags to track the presence of digits, exponent, and decimal point
    has_digit = False
    has_exponent = False
    has_decimal = False
    
    # Iterate over the string
    for i, char in enumerate(s):
        # Check if the character is a digit
        if char.isdigit():
            has_digit = True
        # Check if the character is a decimal point
        elif char == '.':
            # If a decimal point is already present or if it's the last character, return False
            if has_decimal or i == len(s) - 1:
                return False
            has_decimal = True
        # Check if the character is an exponent
        elif char in ['e', 'E']:
            # If an exponent is already present or if it's the first or last character, return False
            if has_exponent or i == 0 or i == len(s) - 1:
                return False
            has_exponent = True
        # Check if the character is a sign
        elif char in ['+', '-']:
            # If the sign is not at the start or after an exponent, return False
            if i != 0 and s[i - 1].lower() != 'e':
                return False
        # If the character is none of the above, return False
        else:
            return False
    
    # Return True if the string contains at least one digit
    return has_digit