def findMiddleIndex(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize the left sum as 0
    left_sum = 0
    
    # Iterate over the array
    for i, num in enumerate(nums):
        # If the left sum equals the total sum minus the left sum and the current number
        # then we have found the middle index
        if left_sum == total_sum - left_sum - num:
            return i
        # Otherwise, add the current number to the left sum
        left_sum += num
    
    # If no middle index is found, return -1
    return -1