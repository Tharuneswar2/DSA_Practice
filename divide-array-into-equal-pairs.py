# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def divideArrayPairs(nums):
    # Create a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Iterate over the array to populate the hashmap
    for num in nums:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Initialize a variable to track the number of pairs
    pairs = 0
    
    # Iterate over the hashmap
    for freq in freq_map.values():
        # If the frequency is even, it means we can form pairs with all occurrences of the number
        if freq % 2 == 0:
            # Increment the pairs count by the frequency divided by 2
            pairs += freq // 2
        # If the frequency is odd, it means we can form pairs with all but one occurrence of the number
        else:
            # Increment the pairs count by the frequency divided by 2 (integer division)
            pairs += freq // 2
    
    # Return True if the total number of pairs is equal to the length of the array divided by 2
    # This means we can divide the array into pairs of equal elements
    return pairs == len(nums) // 2