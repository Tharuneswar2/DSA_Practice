def find_valid_pair(s):
    # Initialize a flag to track if a valid pair is found
    found = False
    
    # Iterate over the string
    for i in range(len(s) - 1):
        # Check if the current character and the next one are digits
        if s[i].isdigit() and s[i + 1].isdigit():
            # If they are, check if they are the same
            if s[i] == s[i + 1]:
                # If they are the same, set the flag to True and break the loop
                found = True
                break
    
    # Return the result
    return found

# Test the function
print(find_valid_pair("abc123"))  # False
print(find_valid_pair("abc1123"))  # True