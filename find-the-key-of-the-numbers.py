def find_key(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the list of numbers
    for num in nums:
        # If the number is already in the dictionary, increment its frequency
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a frequency of 1
        else:
            freq_dict[num] = 1
    
    # Iterate over the dictionary to find the number with the highest frequency
    max_freq = 0
    key = None
    for num, freq in freq_dict.items():
        # If the frequency of the current number is higher than the max frequency, update the max frequency and the key
        if freq > max_freq:
            max_freq = freq
            key = num
    
    # Return the key (the number with the highest frequency)
    return key

# Example usage:
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_key(nums))  # Output: 4