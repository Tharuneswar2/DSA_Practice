# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfPairs(nums):
    # Create a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Initialize the count of pairs
    pairs = 0
    
    # Iterate over the array to populate the hashmap
    for num in nums:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Iterate over the hashmap to calculate the pairs
    for freq in freq_map.values():
        # For each frequency, calculate the pairs by doing integer division by 2
        # This is because each pair consists of 2 numbers
        pairs += freq // 2
    
    # Return the total pairs
    return pairs