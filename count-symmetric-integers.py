# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_symmetric_integers(nums):
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}
    
    # Iterate over the list of integers
    for num in nums:
        # If the integer is already in the dictionary, increment its frequency
        if num in freq_dict:
            freq_dict[num] += 1
        # If the integer is not in the dictionary, add it with a frequency of 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the count of symmetric integers
    symmetric_count = 0
    
    # Iterate over the dictionary items
    for num, freq in freq_dict.items():
        # Check if the negative of the current integer is also in the dictionary
        if -num in freq_dict:
            # If it is, increment the symmetric count by the minimum frequency of the two integers
            symmetric_count += min(freq, freq_dict[-num])
    
    # Return the count of symmetric integers
    return symmetric_count