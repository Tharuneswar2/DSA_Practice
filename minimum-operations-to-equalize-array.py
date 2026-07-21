# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minOperations(nums):
    # First, find the minimum element in the array, as this will be the target value for equalization
    min_val = min(nums)
    
    # Initialize a variable to store the total number of operations required
    operations = 0
    
    # Iterate over each element in the array
    for num in nums:
        # For each element, calculate the difference between the current element and the target value
        # This difference represents the number of operations required to equalize the current element
        operations += num - min_val
    
    # Return the total number of operations required to equalize the entire array
    return operations