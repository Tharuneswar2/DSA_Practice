# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_pairs(nums, k):
    # Initialize a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Initialize the count of pairs to 0
    count = 0
    
    # Iterate over the array to populate the frequency map
    for num in nums:
        # If the number is already in the map, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the map, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Iterate over the array again to count the pairs
    for num in nums:
        # For each number, check if its multiple (num + k) is in the map
        if num + k in freq_map:
            # If it is, increment the count by the frequency of the multiple
            count += freq_map[num + k]
    
    # Return the count of pairs
    return count