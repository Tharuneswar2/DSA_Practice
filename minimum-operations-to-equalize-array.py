def min_operations(nums):
    # Calculate the median of the array
    median = sorted(nums)[len(nums) // 2]
    
    # Initialize the count of operations
    operations = 0
    
    # For each number in the array, calculate the absolute difference with the median
    # This difference represents the number of operations required to equalize the number with the median
    for num in nums:
        operations += abs(num - median)
    
    return operations

# Test the function
print(min_operations([1, 5, 3, 19, 18, 25]))  # Output: 13