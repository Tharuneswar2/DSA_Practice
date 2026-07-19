# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numIdenticalPairs(nums):
    # Create a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Initialize the count of good pairs to 0
    good_pairs = 0
    
    # Iterate over each number in the array
    for num in nums:
        # If the number is already in the hashmap, it means we have seen it before
        if num in freq_map:
            # The number of good pairs that can be formed with this number is equal to its frequency
            # This is because each occurrence of the number can form a pair with every other occurrence
            good_pairs += freq_map[num]
        
        # Increment the frequency of the current number in the hashmap
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Return the total count of good pairs
    return good_pairs