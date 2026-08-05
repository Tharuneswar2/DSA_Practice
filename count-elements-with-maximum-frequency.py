# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countElements(arr):
    # Create a dictionary to store the frequency of each element in the array
    freq_dict = {}
    
    # Iterate over the array to populate the frequency dictionary
    for num in arr:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            freq_dict[num] = 1
    
    # Initialize variables to store the maximum frequency and the count of elements with maximum frequency
    max_freq = 0
    max_freq_count = 0
    
    # Iterate over the frequency dictionary to find the maximum frequency and the count of elements with maximum frequency
    for num, freq in freq_dict.items():
        # If the current frequency is greater than the maximum frequency, update the maximum frequency and reset the count
        if freq > max_freq:
            max_freq = freq
            max_freq_count = 1
        # If the current frequency is equal to the maximum frequency, increment the count
        elif freq == max_freq:
            max_freq_count += 1
    
    # Return the count of elements with maximum frequency
    return max_freq_count