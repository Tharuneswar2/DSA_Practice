def minSubsequence(nums):
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # Initialize variables to store the total sum and the result
    total_sum = sum(nums)
    result = []
    current_sum = 0
    
    # Iterate over the sorted list
    for num in nums:
        # Add the current number to the result and update the current sum
        result.append(num)
        current_sum += num
        
        # If the current sum is greater than the total sum minus the current sum, break the loop
        if current_sum > total_sum - current_sum:
            break
    
    return result