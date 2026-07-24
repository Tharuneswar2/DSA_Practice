# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def splitArray(nums, m):
    # Define the binary search range for the minimum sum
    left, right = max(nums), sum(nums)
    
    # Continue the binary search until the range is narrowed down to a single value
    while left < right:
        # Calculate the mid value of the current range
        mid = (left + right) // 2
        
        # Initialize variables to track the current sum and the number of subarrays
        curr_sum, count = 0, 1
        
        # Iterate over the input array to calculate the number of subarrays required for the current mid value
        for num in nums:
            # If adding the current number to the current sum exceeds the mid value, start a new subarray
            if curr_sum + num > mid:
                curr_sum = num
                count += 1
            # Otherwise, add the current number to the current sum
            else:
                curr_sum += num
        
        # If the number of subarrays required for the current mid value is less than or equal to m, update the right boundary
        if count <= m:
            right = mid
        # Otherwise, update the left boundary
        else:
            left = mid + 1
    
    # Return the minimum sum required to split the array into m subarrays
    return left