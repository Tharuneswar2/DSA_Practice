# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findLucky(arr):
    # Create a dictionary to store the frequency of each number in the array
    freq_dict = {}
    
    # Iterate over the array to populate the frequency dictionary
    for num in arr:
        # If the number is already in the dictionary, increment its frequency
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a frequency of 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the lucky integer
    lucky_int = -1
    
    # Iterate over the frequency dictionary
    for num, freq in freq_dict.items():
        # If the number is equal to its frequency, it's a lucky integer
        if num == freq:
            # If we've already found a lucky integer, return -1
            if lucky_int != -1:
                return -1
            # Otherwise, update the lucky integer
            lucky_int = num
    
    # Return the lucky integer
    return lucky_int