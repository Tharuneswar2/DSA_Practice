def numberOfPairs(nums):
    # Create a hashmap to store the frequency of each number
    freq_map = {}
    
    # Initialize the count of pairs
    pairs = 0
    
    # Iterate over the array to populate the hashmap
    for num in nums:
        # If the number is already in the hashmap, increment its count
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a count of 1
        else:
            freq_map[num] = 1
    
    # Iterate over the hashmap to calculate the number of pairs
    for count in freq_map.values():
        # For each number, the number of pairs is the count divided by 2 (integer division)
        pairs += count // 2
    
    # Return the total number of pairs
    return pairs