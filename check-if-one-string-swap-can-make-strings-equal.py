def areAlmostEqual(s1: str, s2: str) -> bool:
    # If the two strings are equal, we can make them equal with 0 swaps
    if s1 == s2:
        return True
    
    # If the two strings have different lengths or different characters, 
    # we cannot make them equal with one swap
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    
    # Find the indices of the different characters
    diff = [(a, b) for a, b in zip(s1, s2) if a != b]
    
    # If there are more than 2 different characters, we cannot make them equal with one swap
    if len(diff) != 2:
        return False
    
    # If the two different characters are the same but in different order, 
    # we can make them equal with one swap
    return diff[0] == diff[1][::-1]