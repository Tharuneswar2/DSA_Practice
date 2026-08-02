# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minimumOperations(nums):
    # Check if the input list is empty
    if not nums:
        return 0
    
    # Find the minimum non-zero element in the list
    # This is because we can subtract the minimum non-zero element from all elements to make them zero
    min_non_zero = min(num for num in nums if num != 0)
    
    # If all elements are zero, we don't need any operations
    if min_non_zero == float('inf'):
        return 0
    
    # Count the number of operations required to make all elements zero
    # This is equal to the minimum non-zero element
    operations = min_non_zero
    
    # Return the total number of operations
    return operations