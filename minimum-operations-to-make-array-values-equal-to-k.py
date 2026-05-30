def min_operations(nums, k):
    # Calculate the median of the array
    nums.sort()
    median = nums[len(nums) // 2] if len(nums) % 2 != 0 else (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    
    # Initialize the count of operations
    operations = 0
    
    # For each number in the array, calculate the absolute difference with the median
    # and add it to the total operations
    for num in nums:
        operations += abs(num - median)
    
    # Return the total operations
    return operations

def min_operations_to_k(nums, k):
    # Calculate the median of the array
    nums.sort()
    median = nums[len(nums) // 2] if len(nums) % 2 != 0 else (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    
    # If k is equal to the median, no operations are needed
    if k == median:
        return 0
    
    # Initialize the count of operations
    operations = 0
    
    # For each number in the array, calculate the absolute difference with k
    # and add it to the total operations
    for num in nums:
        operations += abs(num - k)
    
    # Return the total operations
    return operations