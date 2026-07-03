def longestEvenOddSubarray(arr, threshold):
    # Initialize variables to store the maximum length and the current sum
    max_len = 0
    curr_sum = 0
    
    # Initialize a hashmap to store the prefix sums and their indices
    prefix_sum = {0: -1}
    
    # Iterate over the array
    for i, num in enumerate(arr):
        # Update the current sum
        curr_sum += num if i % 2 == 0 else -num
        
        # Check if the current sum minus the threshold exists in the hashmap
        if curr_sum - threshold in prefix_sum:
            # Update the maximum length
            max_len = max(max_len, i - prefix_sum[curr_sum - threshold])
        
        # Check if the current sum plus the threshold exists in the hashmap
        if curr_sum + threshold in prefix_sum:
            # Update the maximum length
            max_len = max(max_len, i - prefix_sum[curr_sum + threshold])
        
        # Update the hashmap
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i
    
    return max_len

def longestEvenOddSubarrayAlternative(arr, threshold):
    # Initialize variables to store the maximum length and the current sum
    max_len = 0
    curr_sum = 0
    
    # Initialize a hashmap to store the prefix sums and their indices
    prefix_sum = {0: -1}
    
    # Iterate over the array
    for i, num in enumerate(arr):
        # Update the current sum
        curr_sum += num if i % 2 == 0 else -num
        
        # Check if the current sum minus the threshold exists in the hashmap
        if curr_sum - threshold in prefix_sum:
            # Update the maximum length
            max_len = max(max_len, i - prefix_sum[curr_sum - threshold])
        
        # Check if the current sum plus the threshold exists in the hashmap
        if curr_sum + threshold in prefix_sum:
            # Update the maximum length
            max_len = max(max_len, i - prefix_sum[curr_sum + threshold])
        
        # Update the hashmap
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i
    
    return max_len