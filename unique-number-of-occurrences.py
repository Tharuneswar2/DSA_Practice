# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def uniqueOccurrences(arr):
    # Create a dictionary to store the frequency of each number in the array
    freq_dict = {}
    
    # Iterate through the array to count the frequency of each number
    for num in arr:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            freq_dict[num] = 1
    
    # Create a set to store the unique frequencies
    unique_freqs = set()
    
    # Iterate through the frequency dictionary
    for freq in freq_dict.values():
        # If the frequency is already in the set, return False
        if freq in unique_freqs:
            return False
        # If the frequency is not in the set, add it
        else:
            unique_freqs.add(freq)
    
    # If we've iterated through the entire dictionary without finding any duplicate frequencies, return True
    return True