# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findChampionI(candidates):
    # Initialize a dictionary to store the frequency of each candidate
    frequency = {}
    
    # Iterate over the list of candidates
    for candidate in candidates:
        # If the candidate is already in the dictionary, increment its frequency
        if candidate in frequency:
            frequency[candidate] += 1
        # If the candidate is not in the dictionary, add it with a frequency of 1
        else:
            frequency[candidate] = 1
    
    # Initialize variables to store the champion and its frequency
    champion = None
    max_frequency = 0
    
    # Iterate over the dictionary to find the champion
    for candidate, freq in frequency.items():
        # If the frequency of the current candidate is greater than the max frequency, update the champion and max frequency
        if freq > max_frequency:
            champion = candidate
            max_frequency = freq
    
    # Return the champion
    return champion