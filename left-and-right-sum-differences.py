# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def leftRigthDifference(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum as 0
    left_sum = 0
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the array
    for num in nums:
        # Calculate the right sum by subtracting the left sum and the current number from the total sum
        right_sum = total_sum - left_sum - num
        
        # Calculate the absolute difference between the left sum and the right sum
        difference = abs(left_sum - right_sum)
        
        # Append the difference to the result list
        result.append(difference)
        
        # Update the left sum by adding the current number
        left_sum += num
    
    # Return the result list
    return result