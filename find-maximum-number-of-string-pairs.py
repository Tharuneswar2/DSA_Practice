# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfPairs(nums):
    # Create a hashmap to store the frequency of each number
    freq_map = {}
    
    # Iterate over the list of numbers
    for num in nums:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Initialize a variable to store the total number of pairs
    total_pairs = 0
    
    # Iterate over the hashmap
    for freq in freq_map.values():
        # For each frequency, calculate the maximum number of pairs that can be formed
        # This is done by dividing the frequency by 2 and rounding down to the nearest integer
        total_pairs += freq // 2
    
    # Return the total number of pairs
    return total_pairs