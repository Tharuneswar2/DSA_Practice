def find_pivot(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum to 0
    left_sum = 0
    
    # Iterate over the array
    for num in nums:
        # If the left sum is equal to the total sum minus the left sum and the current number
        # then the current number is the pivot
        if left_sum == total_sum - left_sum - num:
            return num
        # Otherwise, add the current number to the left sum
        left_sum += num
    
    # If no pivot is found, return -1
    return -1

# Test the function
print(find_pivot([1, 7, 3, 6, 5, 6]))  # Output: 3
print(find_pivot([1, 2, 3, 4, 5]))  # Output: -1