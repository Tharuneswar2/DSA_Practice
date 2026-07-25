# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minChanges(self, s: str) -> int:
    # Initialize variables to store the number of changes required for both possible alternating strings
    changes1 = 0
    changes2 = 0
    
    # Initialize the expected characters for both alternating strings
    expected1 = '0'
    expected2 = '1'
    
    # Iterate over the string
    for char in s:
        # If the current character does not match the expected character for the first alternating string, increment changes1
        if char != expected1:
            changes1 += 1
        # If the current character does not match the expected character for the second alternating string, increment changes2
        if char != expected2:
            changes2 += 1
        
        # Flip the expected characters for the next iteration
        expected1 = '1' if expected1 == '0' else '0'
        expected2 = '1' if expected2 == '0' else '0'
    
    # Return the minimum number of changes required
    return min(changes1, changes2)