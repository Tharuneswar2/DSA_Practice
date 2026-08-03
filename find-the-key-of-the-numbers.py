# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_key(nums):
    # Initialize an empty dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the list of numbers to count the frequency of each number
    for num in nums:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the key (the number with the highest frequency)
    key = None
    # Initialize a variable to store the maximum frequency
    max_freq = 0
    
    # Iterate over the dictionary to find the number with the highest frequency
    for num, freq in freq_dict.items():
        # If the frequency of the current number is greater than the maximum frequency, update the key and maximum frequency
        if freq > max_freq:
            max_freq = freq
            key = num
    
    # Return the key (the number with the highest frequency)
    return key