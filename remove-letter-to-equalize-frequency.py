from collections import Counter

def equalFrequency(word):
    # Create a frequency counter for the word
    freq = Counter(word)
    
    # Iterate over each character in the word
    for char in word:
        # Create a copy of the frequency counter
        new_freq = freq.copy()
        
        # Decrement the frequency of the current character
        new_freq[char] -= 1
        
        # If the frequency of the current character is 0, remove it from the counter
        if new_freq[char] == 0:
            del new_freq[char]
        
        # Check if all frequencies in the new counter are equal
        if len(set(new_freq.values())) <= 1:
            return True
    
    # If no character can be removed to equalize the frequency, return False
    return False