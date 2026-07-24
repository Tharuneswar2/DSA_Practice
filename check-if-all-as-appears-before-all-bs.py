# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def check_string(s):
    # Initialize a flag to track if we have encountered 'b' in the string
    encountered_b = False
    
    # Iterate over each character in the string
    for char in s:
        # If we encounter 'b' before 'a', return False
        if char == 'b':
            encountered_b = True
        # If we encounter 'a' after 'b', return False
        elif char == 'a' and encountered_b:
            return False
    
    # If we have iterated over the entire string and haven't returned False, return True
    return True