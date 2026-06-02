def check_string(s):
    # Initialize a flag to track if we've seen a 'b'
    seen_b = False
    
    # Iterate over the string
    for char in s:
        # If we've seen a 'b' and now see an 'a', return False
        if seen_b and char == 'a':
            return False
        # If we see a 'b', set the flag
        elif char == 'b':
            seen_b = True
    
    # If we've iterated over the entire string without returning False, return True
    return True

# Test the function
print(check_string("aaabbb"))  # True
print(check_string("ababab"))  # False