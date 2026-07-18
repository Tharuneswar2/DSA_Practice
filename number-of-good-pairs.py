# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numIdenticalPairs(nums):
    # Create a dictionary to store the frequency of each number in the array
    freq_dict = {}
    
    # Initialize the count of good pairs to 0
    good_pairs = 0
    
    # Iterate over each number in the array
    for num in nums:
        # If the number is already in the dictionary, it means we have seen it before
        if num in freq_dict:
            # The number of good pairs that can be formed with this number is equal to its frequency
            # This is because each occurrence of the number can form a pair with every other occurrence
            good_pairs += freq_dict[num]
            # Increment the frequency of the number by 1
            freq_dict[num] += 1
        else:
            # If the number is not in the dictionary, add it with a frequency of 1
            freq_dict[num] = 1
    
    # Return the total count of good pairs
    return good_pairs