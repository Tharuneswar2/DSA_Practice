def checkAlmostEquivalent(s1: str, s2: str) -> bool:
    # Create a dictionary to store the frequency of each character in both strings
    freq_s1 = {}
    freq_s2 = {}
    
    # Count the frequency of each character in s1
    for char in s1:
        if char in freq_s1:
            freq_s1[char] += 1
        else:
            freq_s1[char] = 1
    
    # Count the frequency of each character in s2
    for char in s2:
        if char in freq_s2:
            freq_s2[char] += 1
        else:
            freq_s2[char] = 1
    
    # Check if the absolute difference in frequency of each character is less than or equal to 3
    for char in set(s1 + s2):
        if abs(freq_s1.get(char, 0) - freq_s2.get(char, 0)) > 3:
            return False
    
    return True