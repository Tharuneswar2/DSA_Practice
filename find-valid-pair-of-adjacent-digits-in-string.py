# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def find_valid_pair(s):
    # Initialize a flag variable to track if a valid pair is found
    found = False
    
    # Iterate over the string from the first character to the second last character
    for i in range(len(s) - 1):
        # Check if the current character and the next character are digits
        if s[i].isdigit() and s[i+1].isdigit():
            # If they are digits, check if they are the same
            if s[i] == s[i+1]:
                # If they are the same, set the flag to True and break the loop
                found = True
                break
    
    # Return the result
    return found

# Test the function
print(find_valid_pair("abc123"))  # False
print(find_valid_pair("abc1123"))  # True