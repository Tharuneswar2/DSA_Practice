# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countUnequalTriplets(nums):
    # Initialize a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Iterate over the array to populate the frequency map
    for num in nums:
        # If the number is already in the map, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the map, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Initialize variables to store the total count of triplets and the count of equal triplets
    total_triplets = 0
    equal_triplets = 0
    
    # Calculate the total count of triplets
    total_triplets = len(nums) * (len(nums) - 1) * (len(nums) - 2) // 6
    
    # Iterate over the frequency map to calculate the count of equal triplets
    for freq in freq_map.values():
        # If the frequency is 3 or more, calculate the count of equal triplets
        if freq >= 3:
            equal_triplets += freq * (freq - 1) * (freq - 2) // 6
    
    # Return the count of unequal triplets
    return total_triplets - equal_triplets