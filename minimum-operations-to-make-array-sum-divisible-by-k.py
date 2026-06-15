def min_operations(nums, k):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # If the total sum is already divisible by k, return 0
    if total_sum % k == 0:
        return 0
    
    # Initialize a hashmap to store the prefix sums modulo k
    prefix_sums = {0: -1}
    current_sum = 0
    min_ops = float('inf')
    
    # Iterate through the array to calculate the prefix sums
    for i, num in enumerate(nums):
        # Update the current sum
        current_sum += num
        
        # Calculate the remainder of the current sum modulo k
        remainder = current_sum % k
        
        # If the remainder is already in the hashmap, update the minimum operations
        if remainder in prefix_sums:
            min_ops = min(min_ops, i - prefix_sums[remainder])
        
        # If the remainder is not in the hashmap, add it
        if remainder not in prefix_sums:
            prefix_sums[remainder] = i
    
    # If no solution is found, return -1
    return min_ops if min_ops != float('inf') else -1