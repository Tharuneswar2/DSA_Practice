# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def equalFrequency(word):
    # Create a frequency dictionary to store the frequency of each character in the word
    freq = {}
    for char in word:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            freq[char] = 1

    # Iterate over each character in the word
    for i in range(len(word)):
        # Create a copy of the frequency dictionary
        new_freq = freq.copy()
        # Decrement the count of the current character in the new frequency dictionary
        new_freq[word[i]] -= 1
        # If the count of the current character becomes 0, remove it from the new frequency dictionary
        if new_freq[word[i]] == 0:
            del new_freq[word[i]]

        # Check if all characters in the new frequency dictionary have the same frequency
        if len(set(new_freq.values())) == 1:
            # If all characters have the same frequency, return True
            return True

    # If no character can be removed to equalize the frequency, return False
    return False