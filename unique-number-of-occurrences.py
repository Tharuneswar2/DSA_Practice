def unique_occurrences(arr):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the array to count the frequency of each number
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Create a set to store the unique frequencies
    unique_freqs = set()
    
    # Iterate over the frequency dictionary to add frequencies to the set
    for freq in freq_dict.values():
        unique_freqs.add(freq)
    
    # If the number of unique frequencies is equal to the number of unique numbers, return True
    return len(unique_freqs) == len(freq_dict)

# Test the function
print(unique_occurrences([1, 2, 2, 1, 1, 3]))  # False
print(unique_occurrences([1, 2]))  # True
print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 3]))  # True