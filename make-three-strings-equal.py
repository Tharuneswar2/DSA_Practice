def makeEqual(words):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for word in words:
        for char in word:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    # Calculate the number of strings
    num_strings = len(words)

    # Check if the frequency of each character is divisible by the number of strings
    for char, freq in char_freq.items():
        if freq % num_strings != 0:
            return False

    return True