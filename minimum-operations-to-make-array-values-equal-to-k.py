# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def min_operations_to_equal_k(arr, k):
    # Calculate the total sum of the array elements
    total_sum = sum(arr)
    
    # If the total sum is less than k times the number of elements, it's impossible to make all elements equal to k
    if total_sum < len(arr) * k:
        return -1
    
    # Initialize the minimum operations count to infinity
    min_operations = float('inf')
    
    # Initialize the prefix sum to 0
    prefix_sum = 0
    
    # Initialize a hashmap to store the prefix sums and their indices
    prefix_sum_indices = {0: -1}
    
    # Iterate over the array
    for i, num in enumerate(arr):
        # Update the prefix sum
        prefix_sum += num
        
        # Calculate the target prefix sum if all elements up to the current index were equal to k
        target_prefix_sum = k * (i + 1)
        
        # If the difference between the target prefix sum and the current prefix sum is in the hashmap
        if target_prefix_sum - prefix_sum in prefix_sum_indices:
            # Update the minimum operations count
            min_operations = min(min_operations, i - prefix_sum_indices[target_prefix_sum - prefix_sum])
        
        # If the current prefix sum is not in the hashmap, add it
        if prefix_sum not in prefix_sum_indices:
            prefix_sum_indices[prefix_sum] = i
    
    # Return the minimum operations count
    return min_operations