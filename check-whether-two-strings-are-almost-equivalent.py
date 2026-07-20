# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def checkAlmostEquivalent(word1, word2):
    # Create a dictionary to store the frequency of each character in both strings
    freq1 = {}
    freq2 = {}
    
    # Iterate over the characters in the first string and update their frequencies
    for char in word1:
        # If the character is already in the dictionary, increment its frequency
        if char in freq1:
            freq1[char] += 1
        # If the character is not in the dictionary, add it with a frequency of 1
        else:
            freq1[char] = 1
    
    # Iterate over the characters in the second string and update their frequencies
    for char in word2:
        # If the character is already in the dictionary, increment its frequency
        if char in freq2:
            freq2[char] += 1
        # If the character is not in the dictionary, add it with a frequency of 1
        else:
            freq2[char] = 1
    
    # Iterate over the characters in the first string's frequency dictionary
    for char in freq1:
        # If the character is not in the second string's frequency dictionary or the difference in frequencies is more than 3, return False
        if char not in freq2 or abs(freq1[char] - freq2.get(char, 0)) > 3:
            return False
    
    # Iterate over the characters in the second string's frequency dictionary
    for char in freq2:
        # If the character is not in the first string's frequency dictionary or the difference in frequencies is more than 3, return False
        if char not in freq1 or abs(freq2[char] - freq1.get(char, 0)) > 3:
            return False
    
    # If no differences in frequencies greater than 3 were found, return True
    return True