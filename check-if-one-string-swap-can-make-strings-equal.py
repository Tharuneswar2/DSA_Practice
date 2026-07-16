# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    # Check if the two strings are equal, if so, return True
    if s1 == s2:
        return True
    
    # If the two strings are not equal, check if they have the same length
    if len(s1) != len(s2):
        return False
    
    # Initialize two lists to store the different characters
    diff1, diff2 = [], []
    
    # Iterate over the characters in the two strings
    for i in range(len(s1)):
        # If the characters at the current position are different
        if s1[i] != s2[i]:
            # Add the characters to the lists
            diff1.append(s1[i])
            diff2.append(s2[i])
    
    # If there are more than two different characters, return False
    if len(diff1) > 2:
        return False
    
    # If there are exactly two different characters
    if len(diff1) == 2:
        # Check if the two characters are swapped
        return diff1[0] == diff2[1] and diff1[1] == diff2[0]
    
    # If there are less than two different characters, return False
    return False