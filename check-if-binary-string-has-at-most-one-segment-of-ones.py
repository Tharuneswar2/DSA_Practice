# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkOnesSegment(s: str) -> bool:
    # Initialize a flag to track if we have encountered a segment of ones
    has_ones_segment = False
    
    # Iterate over the binary string
    for i in range(len(s)):
        # If the current character is '1' and we haven't encountered a segment of ones yet
        if s[i] == '1' and not has_ones_segment:
            # Set the flag to True
            has_ones_segment = True
        # If the current character is '0' and we have encountered a segment of ones
        elif s[i] == '0' and has_ones_segment:
            # If the next character is '1', return False because we have more than one segment of ones
            if i < len(s) - 1 and s[i + 1] == '1':
                return False
    
    # If we have iterated over the entire string and haven't returned False, return True
    return True