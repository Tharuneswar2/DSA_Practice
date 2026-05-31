def numIdenticalPairs(nums):
    # Create a hashmap to store the frequency of each number
    freq_map = {}
    
    # Initialize the count of good pairs
    good_pairs = 0
    
    # Iterate over the list of numbers
    for num in nums:
        # If the number is already in the hashmap, it means we have found a pair
        if num in freq_map:
            # The number of pairs that can be formed with this number is equal to its frequency
            good_pairs += freq_map[num]
        
        # Increment the frequency of the current number
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Return the total count of good pairs
    return good_pairs