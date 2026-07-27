# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def divideArray(nums):
    # Create a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Iterate over the array to populate the hashmap
    for num in nums:
        # If the number is already in the hashmap, increment its count
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a count of 1
        else:
            freq_map[num] = 1
    
    # Iterate over the hashmap to check if all numbers have even frequencies
    for count in freq_map.values():
        # If any number has an odd frequency, return False
        if count % 2 != 0:
            return False
    
    # If all numbers have even frequencies, return True
    return True