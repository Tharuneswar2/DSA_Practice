def waysToSplitArray(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum and count of ways
    left_sum = 0
    count = 0
    
    # Iterate through the array
    for i in range(len(nums) - 1):
        # Add the current element to the left sum
        left_sum += nums[i]
        
        # If the left sum is equal to the total sum minus the left sum, increment the count
        if left_sum == total_sum - left_sum:
            count += 1
    
    # Return the count of ways
    return count

def waysToSplitArray2(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum and count of ways
    left_sum = 0
    count = 0
    
    # Iterate through the array
    for num in nums[:-1]:
        # Add the current element to the left sum
        left_sum += num
        
        # If the left sum is greater than or equal to the total sum minus the left sum, increment the count
        if left_sum >= total_sum - left_sum:
            count += 1
    
    # Return the count of ways
    return count