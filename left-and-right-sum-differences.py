def leftRigthDifference(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum and the result list
    left_sum = 0
    result = []
    
    # Iterate over the array
    for num in nums:
        # Calculate the right sum by subtracting the left sum and the current number from the total sum
        right_sum = total_sum - left_sum - num
        
        # Calculate the absolute difference between the left sum and the right sum
        result.append(abs(left_sum - right_sum))
        
        # Update the left sum by adding the current number
        left_sum += num
    
    return result