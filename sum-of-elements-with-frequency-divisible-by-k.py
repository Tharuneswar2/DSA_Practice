# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sumOfElementsWithFrequencyDivisibleByK(nums, k):
    # Create a hashmap to store the frequency of each element
    freq_map = {}
    
    # Iterate over the list of numbers to populate the frequency map
    for num in nums:
        # If the number is already in the map, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the map, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Initialize a variable to store the sum of elements with frequency divisible by k
    total_sum = 0
    
    # Iterate over the frequency map
    for num, freq in freq_map.items():
        # Check if the frequency of the current number is divisible by k
        if freq % k == 0:
            # If it is, add the number multiplied by its frequency to the total sum
            total_sum += num * freq
    
    # Return the total sum
    return total_sum