def numberOfSubarrays(nums):
    # Initialize variables to store the count of subarrays and the current sum
    count = 0
    current_sum = 0
    
    # Initialize a hashmap to store the frequency of sums
    sum_freq = {0: 1}
    
    # Iterate over the array
    for num in nums:
        # Update the current sum
        current_sum += num
        
        # If the current sum is even, it means we have found a subarray with an odd number of 1s
        if current_sum % 2 == 0:
            # Increment the count by the frequency of the current sum minus 1
            count += sum_freq.get(current_sum - 1, 0)
        
        # Increment the frequency of the current sum
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
    
    # Return the count of subarrays
    return count