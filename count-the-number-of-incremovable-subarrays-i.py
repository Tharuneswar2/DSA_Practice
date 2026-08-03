# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfSubarrays(nums):
    # Initialize variables to store the count of subarrays and the current prefix sum
    count = 0
    prefix_sum = 0
    
    # Initialize a hashmap to store the frequency of prefix sums
    prefix_sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1
    
    # Iterate over the array
    for num in nums:
        # Update the prefix sum
        prefix_sum += num
        
        # If the prefix sum is already in the hashmap, it means we have found a subarray with sum 0
        # So, add the frequency of this prefix sum to the count
        if prefix_sum in prefix_sum_freq:
            count += prefix_sum_freq[prefix_sum]
        
        # Update the frequency of the current prefix sum
        prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1
    
    # Return the count of subarrays
    return count