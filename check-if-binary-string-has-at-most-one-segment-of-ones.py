def check_ones_segment(s: str) -> bool:
    # Initialize a flag to track if we've seen a segment of ones
    seen_ones = False
    
    # Iterate over the string
    for i in range(len(s)):
        # If we see a '1', check if we've already seen a segment of ones
        if s[i] == '1':
            # If we've already seen a segment of ones, return False
            if seen_ones:
                return False
            # Otherwise, mark that we've seen a segment of ones
            seen_ones = True
        # If we see a '0' after seeing a segment of ones, reset the flag
        elif seen_ones:
            seen_ones = False
    
    # If we've iterated over the entire string without returning False, return True
    return True